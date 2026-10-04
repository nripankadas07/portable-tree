import argparse,json,os,re,unicodedata
from pathlib import Path
RESERVED=re.compile(r'^(CON|PRN|AUX|NUL|COM[1-9¹²³]|LPT[1-9¹²³])(?:\.|$)',re.I)
def _scan_error(error):
    raise error
def audit(root):
    root=Path(root)
    if not root.is_dir(): raise ValueError('root must be an existing directory')
    findings=[]; count=0
    for parent,dirs,files in os.walk(root,followlinks=False,onerror=_scan_error):
        dirs[:]=sorted(d for d in dirs if d!='.git'); groups={}
        for name in sorted(dirs+files):
            count+=1; rel=(Path(parent)/name).relative_to(root).as_posix()
            key=unicodedata.normalize('NFC',name).casefold().rstrip(' .')
            groups.setdefault(key,[]).append(rel)
            reasons=[]
            if RESERVED.match(name): reasons.append('windows_reserved')
            if any(ord(c)<32 or c in '<>:"/\\|?*' for c in name): reasons.append('windows_invalid_character')
            if name.endswith((' ','.')): reasons.append('windows_trailing_character')
            if len(name.encode('utf-8'))>255: reasons.append('utf8_component_over_255_bytes')
            if unicodedata.normalize('NFC',name)!=name: reasons.append('non_nfc_name')
            if (Path(parent)/name).is_symlink(): reasons.append('symlink_not_followed')
            for reason in reasons: findings.append({'kind':reason,'paths':[rel]})
        for paths in groups.values():
            if len(paths)>1: findings.append({'kind':'normalized_sibling_collision','paths':paths})
    return {'entries':count,'findings':sorted(findings,key=lambda x:(x['kind'],x['paths']))}
def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('root');a=p.parse_args()
    try: result=audit(a.root)
    except (ValueError,OSError) as e: p.exit(2,str(e)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2)); return int(bool(result['findings']))
if __name__=='__main__': raise SystemExit(main())

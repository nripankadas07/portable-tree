import tempfile,json
from pathlib import Path
from portable_tree import audit
with tempfile.TemporaryDirectory() as d:
 for n in ['README','Readme','CON.txt']:Path(d,n).touch()
 print(json.dumps(audit(d),indent=2))

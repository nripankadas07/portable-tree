import tempfile,unittest,os
from pathlib import Path
from portable_tree import audit
class Tests(unittest.TestCase):
 def test_collision_reserved_unicode(self):
  with tempfile.TemporaryDirectory() as d:
   for n in ['Readme','README','NUL.txt','COM¹.txt','café','cafe\u0301']:Path(d,n).touch()
   kinds=[x['kind'] for x in audit(d)['findings']]
   self.assertEqual(kinds.count('normalized_sibling_collision'),2);self.assertIn('windows_reserved',kinds);self.assertIn('non_nfc_name',kinds)
 def test_nested_names_do_not_collide(self):
  with tempfile.TemporaryDirectory() as d:
   for n in ['a','b']:Path(d,n).mkdir();Path(d,n,'readme').touch()
   self.assertEqual(audit(d)['findings'],[])
 def test_symlink_cycle_not_followed(self):
  with tempfile.TemporaryDirectory() as d:
   os.symlink(d,Path(d,'loop'));r=audit(d);self.assertEqual(r['entries'],1);self.assertEqual(r['findings'][0]['kind'],'symlink_not_followed')
 def test_invalid_root(self):
  with self.assertRaises(ValueError):audit('/definitely-missing-portable-tree')

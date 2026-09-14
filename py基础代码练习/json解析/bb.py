from pathlib import Path
import json

path=Path('ab.json')
user={}
contents=path.read_text()
user=json.loads(contents)
print(user)
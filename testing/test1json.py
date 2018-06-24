import json
s = "[['a','b','c','d'],['x','y','z']]"
out = json.loads(s.replace("'", '"'))

print(out)
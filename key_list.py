import json
from ordered_set import OrderedSet 
with open('data/link2req.json', 'r', encoding='utf8') as json_file:
    loaded_json = json.loads(json_file.read())
titles = OrderedSet()
titles.update('ID')
for k,v in loaded_json.items():
	#print(v.keys())
	for title in v.keys():
		titles.update([title])
print(list(titles))
 
f = open('data/link 2/link2req.csv', 'w')

f.write("ID |")


import json

with open('data/req_2.json', 'r', encoding='utf8') as json_file:
    loaded_json = json.loads(json_file.read())


reverse =  open('data/reverse_2.json', 'w', encoding='utf8')
# reverse = json.loads(reverse.read())


highest = 0 
for k,v in loaded_json.items():
	for a,b in k:
	# 	print(key, value)
		print(type(k))
		v.keys()
		v.values()
		


	break




import json
f = open('data/link 2/link2req.csv', 'a')
with open('data/link2req.json', 'r', encoding='utf8') as json_file:
    loaded_json = json.loads(json_file.read())
titles = ['募集職種名', '仕事詳細', '雇用形態', '勤務地（都道府県）', '勤務地（住所）', '勤務時間', '交通', '給与・年収', '休日・休暇', '掲載終了予定日', 'モデル年収', '配属部署', '待遇・福利厚生', '教育制度', 'スキル・経験']
value = ""
for k,v in loaded_json.items():
	print(k)
	value = k+"|" #set id to output string
	for title in titles:
		if str(title) in v.keys():
			value = value + str(v[title]) + "|"
		else:
			value = value + " |"
	f.write(value+"\n")
	

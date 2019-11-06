import datetime
import os

x = datetime.datetime.now()
directory = str(x.strftime("%A-%X"))

#ensure no same directory exists
if not os.path.exists(str("data/"+directory)):
	os.makedirs(str("data/"+directory))

if os.path.exists(str("data/"+directory)):
	csvFile = "result_in_csv"+".csv"
	jsonFile = "result_in_json"+".json"
	idList = "company_id_list"+".csv"

	try:
		file = open(str("data/"+directory+"/")+csvFile, 'r')
		file.close()
		file = open(str("data/"+directory+"/")+jsonFile, 'r')
		file.close()
		file = open(str("data/"+directory+"/")+idList, 'r')
		file.close()
	except IOError:
		file = open(str("data/"+directory+"/")+csvFile, 'w')
		file.close()
		file = open(str("data/"+directory+"/")+jsonFile, 'w')
		file.close()
		file = open(str("data/"+directory+"/")+idList, 'w')
		file.close()

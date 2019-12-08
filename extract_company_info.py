from bs4 import BeautifulSoup as bs
import urllib.request
import re
import json
from collections import OrderedDict

###########
# This program collects the information from the houjin website. 
#
#
#
#############
iteration = 0
limit = 10

#get ids file and iterate

# for n in range(1, 13):
for industry in range(1,13):
    companyUrls = open('data/'+str(industry)+'.csv').read().split()
    all_data = OrderedDict()
    for url in companyUrls:
        data = OrderedDict()
        print(url)
        #fetch the html of the particular job listing
        try:
            page = urllib.request.urlopen(str(url))
        except:
            print("An error occured.") 
       
        try: 
            soup = bs(page, 'html.parser')
            table = soup.find_all('table')[0]
            industry_name = soup.find("span", "industry-item")
            try:
                industry_name = industry_name.a.text
                
            except:
                industry_name = "業界未設定"
            company_id = table.tr.td.text
            # print(company_id)
            for i in table:
                # print(i.th.text+" "+i.td.text)
                data['Industry'] = industry_name
                data[i.th.text] = i.td.text

            all_data[company_id] = data
            with open('data/data'+str(industry)+'.json', 'w', encoding='utf8') as json_file:
                json.dump(all_data, json_file, ensure_ascii=False)
                json_file.close()
        except:
            pass
    
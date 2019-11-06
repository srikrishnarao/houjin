#2  Information about the company and job, url and location of the job 

#https://careerindex.jp/job_offers/36836422
from bs4 import BeautifulSoup as bs
import urllib.request
import re
import json

iteration = 0
limit = 10

#get ids file and iterate

job_numbers = open('data/comp2_ids.csv').read().split()
all_data = {}


for job_number in job_numbers:
    
    #fetch the html of the particular job listing
    number = str(job_number)
    url = "https://careerindex.jp/job_offers/"+number
    try:
        page = urllib.request.urlopen(url)
    except:
        print("An error occured.")
    soup = bs(page, 'html.parser')

    requirements_data = soup.find_all('div', attrs={'class': 'requirements__data'})
    requirements_head = soup.find_all('div', attrs={'class': 'requirements__head'})
    
    data_keys = [] 
    data_values = []
    
    for i in requirements_head:
        head = bs(str(i), 'html.parser')
        data_keys.append(head.text)
    for i in requirements_data:
        data = bs(str(i), 'html.parser')
        data_values.append(data.text)
        
    zipper = zip(data_keys, data_values)
    
    data_dict = dict(zipper)
    print(data_dict)
    all_data[job_number] = data_dict
    print(job_number)

    # loop 
    if iteration>limit:
        break
    iteration = iteration + 1

print("\n")
print("Data Extraction completed ")  


with open('data/result_2.json', 'w', encoding='utf8') as json_file:
    json.dump(all_data, json_file, ensure_ascii=False)
# 1 List of the companies ande

from bs4 import BeautifulSoup as bs
import urllib.request
import re


links = []
f_ids = open('data/company_ids.csv', 'a')
i = 1
pageNumber = 100# number of pages to be searched
while(i<pageNumber+1):
    number = str(i)
    url = "https://houjin.jp/search?page="+number
    #print(url)
    try:
        page = urllib.request.urlopen(url)
    except:
        print("An error occured.")
    print("Data fetched for page", i)
    
    soup = bs(page, 'html.parser')
    
    for a in soup.find_all('a', href=True):
        if re.match('^/c/', a['href']):
            f_ids.write("https://houjin.jp"+a['href']+"\n")
    
    i=i+1
f_ids.close() 


          

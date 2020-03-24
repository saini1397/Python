# importing required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import re

os.chdir('C:/Users/Python/Output/WebScrap')

srch = input("Enter your Search -->")

# target URL to scrap , here we are using a dummy website shopme.com replace it with the site you want to scarp from.
url = "https://www.shopme.com/search?q="+srch+"&otracker=search&otracker1=search&marketplace=shome&as-show=on&as=off&sort=popularity"
print(url)



# headers
headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    }
response = requests.request("GET", url, headers=headers)
data = BeautifulSoup(response.text, 'html.parser')

pg = data.find('div', attrs={'class', '_2zg3yZ'})
print(pg)
if pg == None:
    msg = "No Data/Page Found"
    print(msg)
else:    
 pg_list = []
 dfs = pd.DataFrame()
 pg_list =  pg.text[10:13]
 pg_list=re.sub("\D", "", pg_list) #Convert non-digit to missing
  
 print(pg_list)
 pg_no = int(pg_list)
 j=1
 while j<=pg_no:
     print(j)
     url_nw = url+"&page="+str(j)
     print(url_nw)
     response = requests.request("GET", url_nw, headers=headers)
     data = BeautifulSoup(response.text, 'html.parser')
    
     cards_data = data.find_all('div', attrs={'class', '_3liAhj'})
     print('Total Number of Cards Found : ', len(cards_data))
     # create a list to store the data
     scraped_data = []
    
     if len(cards_data) == 0:
         j=j+1
         break
    
     for card in cards_data:
       
        card_details = {}
        item_name = card.find('a',attrs={'class': '_2cLu-l'})
        item_price = card.find('div',attrs={'class': '_1vC4OE'})
        rev = card.find('div',attrs={'class': 'hGSR34'})
        if rev != None:
           review = card.find('div',attrs={'class': 'hGSR34'})
    
        card_details['Product'] = item_name.text
        card_details['Price'] = item_price.text.strip("₹")
        if rev != None: 
           card_details['Review'] = review.text
     # append the scraped data to the list
        scraped_data.append(card_details)

# create a data frame from the list of dictionaries
       
        df = pd.DataFrame.from_dict(scraped_data)
        dfs=pd.concat([dfs,df],ignore_index=True,sort=True).drop_duplicates(keep='first')
    #dfs.to_csv('shopme_data.csv',index=False)
     j=j+1
 dfs.to_csv('shopme_data.csv',index=False)        
 

import requests
from bs4 import BeautifulSoup as bs

import pandas as pd


def get_news_from_div1(raw):
    
    try:
        
        #get title

        title= raw.find_all('h3')[0].a.contents[0]

        #get date
        date= raw.find_all('time',class_='time')[0]['content'].split('T')[0]

        #get link
        link= raw.find_all('h3')[0].a.get('href')

        return [title,link,1,date ]
    except :
        return None

def get_raw_list_news1(url,year_stop):

    try:
        page= requests.request('GET',url)
        soup= bs(page.text)

        if page.status_code !=200: 
          return -2,[]

        


        #div section
        filter1=soup.body.find_all('div')[2].find_all('section')[0] 
        
        #div cf
        filter2= filter1.find_all('div',class_="cf")[-10]

        #div "row mb..." has list div of news
        filter1=soup.find_all('div',class_="posts border ajaxify-pagination")[0]

        # listing news div
        list_news=filter1.find_all('article')

        ex= list_news[0]
        year=ex.find_all('time',class_='time')[0]['content']

        year=int(year.split('-')[0])
        print(year)
        if year < year_stop:
            return -1,[]

        return page.status_code,list_news
    except ValueError:
        return -2,[]


url='https://www.thebeaverton.com/page/{}/'

count_failed=0
data1=[] 
for i in range(600):
  response , ls_news= get_raw_list_news1(url.format(i),2018)

  if response==-1: 
      print(1)
      break
  if response==400:
      print(2)
      count_failed+=1
      continue
  if len(ls_news)!=0:
      #print(3)
      for x in ls_news:
          temp= get_news_from_div1(x)
          if temp is not None:
              data1.append(temp)


df=pd.DataFrame(data=data1,columns=['headline','article_link','is_sarcastic','date'])

df.to_csv('beaverton.csv')
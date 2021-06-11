

import requests
from bs4 import BeautifulSoup as bs

import pandas as pd


def get_news_from_div(raw,url):
    
    try:
        url= url.split('/news')[0]
        #get title
        title= raw.split(':title=')[1].split(':image')[0]
        title= html.unescape(title)[2:-3]

        #get date
        date=raw.split(':published_on=')[1].split(':primary_category')[0][2:-3]

        #get link
        link= raw.split(':path=')[1].split(':is_premium=')[0][2:-3]
        return [title,url+link,1,date ]
    except :
        return None


def get_raw_list_news(url,year_stop):

    try:
        page= requests.request('GET',url)
        text= page.text

      

        #div body
        filter1= text.split('<body class="">')[1]
        filter1= filter1.split('</body>')[0]
        
        #div main
        filter2= filter1.split('main class="py-4"')[1]
        filter2= filter2.split('</main>')[0]

        #div "row mb..." has list div of news
        filter3= filter2.split('<div class="row mb-2 gutter-4">')[1]
        filter3= filter3.split('<ul class="pagination" role="navigation">')[0]

        # listing news div
        list_news= filter3.split('<div class="col-sm-6">')

        year=int(get_news_from_div(list_news[2],url)[-1].split(',')[-1])
        print(year)
        if year < year_stop:
            return -1,[]

        return page.status_code,list_news
    except ValueError:
        return -2,[]



url='https://babylonbee.com/news?page={}'

count_failed=0
data=[] 
for i in range(350):
  response , ls_news= get_raw_list_news(url.format(i),2018)

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
          temp= get_news_from_div(x,url)
          if temp is not None:
              data.append(temp)

df=pd.DataFrame(data=data,columns=['headline','article_link',,'is_sarcastic','date'])

df.to_csv('babylon.csv')
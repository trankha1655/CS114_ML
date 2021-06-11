

import requests
from bs4 import BeautifulSoup as bs

import pandas as pd

def get_info(x):
  filter1 =x.find('a',class_='title')
  filter2 =x.find('span')

  tilte= filter1.get_text()
  link=  filter1.get('href')
  date=  filter2.get_text()
  return [tilte,link,0,date]




url="https://toronto.citynews.ca/category/national/page/{}/"

data=[]
for i in range(2500):
  page= requests.request('GET',url.format(i))
  soup= bs(page.text)
  list_news=soup.find_all('div',class_='post_row col-lg-16 col-md-16 col-sm-16 col-xs-16')

  date= list_news[0].find('span').get_text()
  year= date.split(', ')[1].split(' ')[0]
  

  if int(year) <2018:
    break
  
  for x in list_news:
    temp= get_info(x)
    if temp is not None:
      data.append(temp)




df_kha3=pd.DataFrame(data=data1,columns=['headline','article_link','is_sarcastic','date'])
df_kha3

df_kha3.to_csv('citynews.csv')
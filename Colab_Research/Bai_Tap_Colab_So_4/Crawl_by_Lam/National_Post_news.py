import requests
from bs4 import BeautifulSoup
from datetime import date , timedelta
from tqdm import tqdm
import time
import pandas as pd


link5 = "https://nationalpost.com/search/?search_text=news&date_range=-7300d&sort=desc&from="


def get_data5(link5):
  response = requests.get(link5)
  lst = []
  soup = BeautifulSoup(response.content, "html.parser")
  table  = soup.findAll('div', class_="article-card__content") #Tìm list bài báo
  times = []
  for i in table: #tìm thẻ span chứa ngày tháng năm phát hành bài báo
    time = []
    z = i.find('div') 
    for j in z:
      k = j.find('span')
      time.append(k)
    year = time[3].text[-5:]
    try :
      if (year == ' ago '):
        times.append(2021)
      else:
        times.append(int(year))
    except:
      times.append(2018)
  links = [link.find('a').attrs["href"] for link in table] #tìm các đường link bài báo
  headline = []    #find headline
  for link in table: #Tìm tiêu đề bài báo
    text = link.find('a').text.split('   ') 
    headline.append(text[0])
  for i in range(len(links)):
    dic = dict()
    dic["article_link"] = "https://nationalpost.com/"+ links[i]
    dic["headline"] = headline[i]
    dic["is_sarcastic"] = 0
    
    if (int(times[i])> 2018): #thêm nhưng bài báo phát hành sau năm 2018
      lst.append(dic)
  return lst  

def extra_csv(lst):
  headline = []
  article_link = []
  is_sarcastic = []
  for i in lst:
    article_link.append(i['article_link'])
    headline.append(i['headline'])
    is_sarcastic.append(i['is_sarcastic'])
  df = pd.DataFrame({'headline':headline,'article_link':article_link,'is_sarcastic':is_sarcastic})
  return df


lst = []
for index in tqdm(range(0, 10000,10)): #tìm kiếm 10000 bài báo
  link = link5 + str(index)
  lst += get_data5(link)



df =extra_csv(lst)
df['date']= [None]*10000
df.to_csv('TheTrueNorthTime.csv')
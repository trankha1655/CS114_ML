import requests
from bs4 import BeautifulSoup
import pandas as pd



from datetime import date,timedelta
today = date.today()
d = today.strftime("%Y/%m/%d")


headline = []
article_link = []
is_sarcastic = []
date = []
link = 'https://www.euronews.com/' # Đường dẫn đến trang web
while(today.year>=2019):
  req = requests.get(link+d) # d là yyyy/mm/dd
  print(req)
  if(req.status_code==200): # Kiểm tra request thành công hay không?
    soup = BeautifulSoup(req.text, "lxml")

    for i in soup.find_all('a',class_ = 'm-object__title__link '):
      headline.append(i.get('title')) #Lấy tiêu đề 
      article_link.append('https://www.euronews.com/'+i.get('href')) #Lấy URL
      is_sarcastic.append(0)
      date.append(d)
  
  today -= timedelta(1)
  d = today.strftime("%Y/%m/%d")

df = pd.DataFrame({'headline':headline,'article_link':article_link,'is_sarcastic':is_sarcastic,'date':date})


df.to_csv('euronews.csv')
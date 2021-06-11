import requests
from bs4 import BeautifulSoup
import pandas as pd



headline = []
article_link = []
is_sarcastic = []
date = []

title_news=["news","humor"]
link = 'https://www.newyorker.com/latest/{}/page/{}' #Đường dẫn đến trang web theo page

for news in title_news:
  for i in range(400):
    req = requests.get(link.format(news,i)) #Tạo request
    soup = BeautifulSoup(req.text, "lxml")
    g = soup.find_all('div',class_='River__riverItemContent___2hXMG') #Tìm tất cả thẻ chứa thông tin bài báo

    ex= g[0]
    year= int(ex.find_all('h6',class_="River__publishDate___1fSSK")[0].get_text().split(', ')[-1])

    if year <2018:
      break

    for i in g:
      headline.append(i.find('a',class_='Link__link___3dWao ').get_text()) #Lấy tiêu đề
      url = 'https://www.newyorker.com/' + i.find('a',class_='Link__link___3dWao ').get('href') #Lấy URL
      article_link.append(url)
      date.append(i.find('h6').get_text()) #Lấy ngày phát hành
      is_sarcastic.append(1) #Lable


df = pd.DataFrame({'headline':headline,'article_link':article_link,'is_sarcastic':is_sarcastic,'date':date})


df.to_csv('newyorker.csv')








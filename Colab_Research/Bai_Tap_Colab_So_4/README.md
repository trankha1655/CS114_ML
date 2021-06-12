#  CRAWL DATA FROM NEWSPAPER WEB

## Các trang web lấy data:

### is_sarcastic
 - [**The Babylon Bee**](https://babylonbee.com/news)
 - [**The Beaverton**](https://www.thebeaverton.com/)
 - [**The New Yorker**](https://www.newyorker.com/)
### is-not_sarcastic
 - [**Euronews**](https://www.euronews.com)
 - [**CityNews Toronto**](https://toronto.citynews.ca/category/national/)
 - [**National Post**](https://nationalpost.com/)
 
## Usage
### Requirement
 - pandas
 - requests
 - bs4
 - tqdm
 - datetime

```
$ conda install -r requirement.txt
```

### Crawl news from Web
```
#code by Kha
python Crawl_by_Kha\Babylon_news.py
python Crawl_by_Kha\beveaton_news.py
python Crawl_by_Kha\citynews_news.py
```
```
#code by Lam
python Crawl_by_Lam\National_Post_news.py
```
```
#code by Nghia
python Crawl_by_Nghia\Euronews_news.py
python Crawl_by_Nghia\The_Newyorker_news.py
```
```
#merge all csv-file to one file
python merge.py
```
```
#convert csv to json
python convert_csv_to_json.py
```
## Nhận xét
Tổng kết quá trình thu thập tiêu đề bài báo, nhóm thu thập được tổng cộng 78234 tiêu đề bài báo. Trong đó:
1. Các trang báo châm biếm:
- The Babylon Bee: 3470 tiêu đề
- The Baeverton: 5565 tiêu đề
- Borowitz Report (Newyorker): 4420 tiêu đề
2. Các trang báo chính thống:
- CityNews: 30778 tiêu đề
- National Post: 9999 tiêu đề
- Euronews: 24002 tiêu đề

Mỗi trang web có các cách crawl data khác nhau do tổ chức cấu trúc trang web khác nhau và nhóm sử dụng thư viện BeautifulSoup của python để crawl data trên các trang báo. Số lượng tiêu đề báo châm biếm ít hơn báo chính thống vì các trang chính thống đăng rất nhiều thông tin về nhiều lĩnh vực còn các trang châm biếm có số lượng báo ra mỗi ngày rất hạn chế.

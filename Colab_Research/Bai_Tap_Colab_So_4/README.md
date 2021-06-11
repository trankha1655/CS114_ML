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
## Nhận xét


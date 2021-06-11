import pandas as pd 


df_nghia1= pd.read_csv('Crawl_by_Nghia\euronews.csv',index_col=0)
df_nghia2= pd.read_csv('Crawl_by_Nghia\newyorker.csv')

df_kha1= pd.read_csv('Crawl_by_Kha\beaverton.csv',index_col=0)
df_kha2= pd.read_csv('Crawl_by_Kha\babylon.csv',index_col=0)
df_kha3= pd.read_csv('Crawl_by_Kha\citynews.csv',index_col=0)

df_lam = pd.read_csv('Crawl_by_Lam\TheTrueNorthTime.csv',index_col=0)

df= pd.DataFrame()
df = df_kha2.append((df_kha3,df_kha1,df_nghia1,df_nghia2,df_lam))


df.to_csv('data_crawl.csv',index=False)
import pandas as pd
import json


data = pd.read_csv('dataset-news-is_sarcastic.csv')
data.drop(columns=['Unnamed: 0','date'],inplace=True)
data = data[['article_link','headline','is_sarcastic']]




json_path = 'dataset-news-is_sarcastic.json'
jsonfile = open(json_path, 'w')
data = data.to_dict(orient='records')
for row in data:
  json.dump(row,jsonfile)
  jsonfile.write('\n')
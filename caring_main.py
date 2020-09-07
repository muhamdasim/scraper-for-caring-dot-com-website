import pandas as pd
import caring_scraper as scraper
df=pd.read_csv('urls.csv')
urls=df.values.tolist()





scraper.test()
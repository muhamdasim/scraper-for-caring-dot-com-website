import pandas as pd
import caring_scraper as scraper
df=pd.read_csv('urls.csv')
urls=df.values.tolist()

#Page Requests

soup=scraper.pageRequest('https://www.caring.com/senior-living/washington/seattle/merrill-gardens-at-first-hill-98101')

print(scraper.pageTitle(soup))
print(scraper.MetaDescription(soup))
print(scraper.communityName(soup))
print(scraper.getCommunityStreetAddress(soup))
print(scraper.getCommunityCity(soup))
print(scraper.getCommunityState(soup))
print(scraper.getCommunityZipCode(soup))
print(scraper.getCommunityImages(soup))
print(scraper.getCommunityContent(soup))
print(scraper.getAverageReviewScore(soup))
print(scraper.getAltTags(soup))
print(scraper.getImageTitle(soup))
print("Testing Phase")
bulk=scraper.test(soup)
for i in bulk:
    if (i=="Costs"):
        for k in soup.find(class_='attribute-group').findAll('li'):
            print(k.get_text().strip())
import pandas as pd
import caring_scraper as scraper
df=pd.read_csv('urls.csv')
urls=df.values.tolist()

#list definitions
pageTitle=[]
metaDescription=[]
communityName=[]
communityStreetAddress=[]
communityCity=[]
communityState=[]
communityZipCode=[]
communityImages=[]
altTags=[]
imageTitle=[]
communityContent=[]
averageReviewScore=[]
costs=[]
roomHousingOptions=[]
diningOptions=[]
features=[]
cleaningServices=[]
techEntertainment=[]
healthServices=[]
activities=[]
financialGuidance=[]
guestServices=[]
languagues=[]
general=[]
typeOfCare=[]
trainingAreas=[]
licenses=[]

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
print(scraper.getAltTags(soup))
print(scraper.getImageTitle(soup))
print(scraper.getCommunityContent(soup))
print(scraper.getAverageReviewScore(soup))
bulk=scraper.test(soup)
for i in bulk:
    if i=="Costs":
        for k in soup.findAll(class_="attribute-group"):
            if k.find(class_='text-body').get_text().strip()==i:
                for z in k.findAll('li'):
                    costs.append(z.get_text().strip())

    elif i=="ROOM AND HOUSING OPTIONS":
        for k in soup.findAll(class_="attribute-group"):
            if k.find(class_='text-body').get_text().strip()==i:
                for z in k.findAll('li'):
                    roomHousingOptions.append(z.get_text().strip())

    elif i=="Dining options":
        for k in soup.findAll(class_="attribute-group"):
            if k.find(class_='text-body').get_text().strip()==i:
                for z in k.findAll('li'):
                    diningOptions.append(z.get_text().strip())
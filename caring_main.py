import pandas as pd
import caring_scraper as scraper
urls=[]
df = pd.read_csv('urls.csv')
for i in df['urls']:
    urls.append(i)

# list definitions
pageTitle = []
metaDescription = []
communityName = []
communityStreetAddress = []
communityCity = []
communityState = []
communityZipCode = []
communityImages = []
altTags = []
imageTitle = []
communityContent = []
averageReviewScore = []
costs = []
roomHousingOptions = []
diningOptions = []
features = []
cleaningServices = []
techEntertainment = []
healthServices = []
activities = []
financialGuidance = []
guestServices = []
languagues = []
general = []
typeOfCare = []
trainingAreas = []
licenses = []

# Page Requests

counter=0
print(len(urls))

for i in urls:
    soup=scraper.pageRequest(i)
    print("Scraping:",i)
    counter+=1
    if(counter==3):
        break
    pageTitle.append(scraper.pageTitle(soup))
    metaDescription.append(scraper.MetaDescription(soup))
    communityName.append(scraper.communityName(soup))
    communityStreetAddress.append(scraper.getCommunityStreetAddress(soup))
    communityCity.append(scraper.getCommunityCity(soup))
    communityState.append(scraper.getCommunityState(soup))
    communityZipCode.append(scraper.getCommunityZipCode(soup))
    communityImages.append(scraper.getCommunityImages(soup))
    altTags.append(scraper.getAltTags(soup))
    imageTitle.append(scraper.getImageTitle(soup))
    communityContent.append(scraper.getCommunityContent(soup))
    averageReviewScore.append(scraper.getAverageReviewScore(soup))
    bulk = scraper.test(soup)
    for i in bulk:
        if i == "Costs":
            for k in soup.findAll(class_="attribute-group"):
                if k.find(class_='text-body').get_text().strip() == i:
                    for z in k.findAll('li'):
                        costs.append(z.get_text().strip())

        elif i == "ROOM AND HOUSING OPTIONS":
            for k in soup.findAll(class_="attribute-group"):
                if k.find(class_='text-body').get_text().strip() == i:
                    for z in k.findAll('li'):
                        roomHousingOptions.append(z.get_text().strip())

        elif i == "Dining options":
            for k in soup.findAll(class_="attribute-group"):
                if k.find(class_='text-body').get_text().strip() == i:
                    for z in k.findAll('li'):
                        diningOptions.append(z.get_text().strip())

        elif i == "Fetures":
            for k in soup.findAll(class_="attribute-group"):
                if k.find(class_='text-body').get_text().strip() == i:
                    for z in k.findAll('li'):
                        features.append(z.get_text().strip())

        elif i == "Cleaning services":
            for k in soup.findAll(class_="attribute-group"):
                if k.find(class_='text-body').get_text().strip() == i:
                    for z in k.findAll('li'):
                        cleaningServices.append(z.get_text().strip())

        elif i == "Technology and entertainment":
            for k in soup.findAll(class_="attribute-group"):
                if k.find(class_='text-body').get_text().strip() == i:
                    for z in k.findAll('li'):
                        techEntertainment.append(z.get_text().strip())

        elif i == "Health services":
            for k in soup.findAll(class_="attribute-group"):
                if k.find(class_='text-body').get_text().strip() == i:
                    for z in k.findAll('li'):
                        healthServices.append(z.get_text().strip())

        elif i == "Activities":
            for k in soup.findAll(class_="attribute-group"):
                if k.find(class_='text-body').get_text().strip() == i:
                    for z in k.findAll('li'):
                        activities.append(z.get_text().strip())
        elif i == "Financial guidance":
            for k in soup.findAll(class_="attribute-group"):
                if k.find(class_='text-body').get_text().strip() == i:
                    for z in k.findAll('li'):
                        financialGuidance.append(z.get_text().strip())

        elif i=="Guest services":
            for k in soup.findAll(class_="attribute-group"):
                if k.find(class_='text-body').get_text().strip() == i:
                    for z in k.findAll('li'):
                        guestServices.append(z.get_text().strip())

        elif i=="Languages":
            for k in soup.findAll(class_="attribute-group"):
                if k.find(class_='text-body').get_text().strip() == i:
                    for z in k.findAll('li'):
                         languagues.append(z.get_text().strip())

        elif i=="General":
            for k in soup.findAll(class_="attribute-group"):
                if k.find(class_='text-body').get_text().strip() == i:
                    for z in k.findAll('li'):
                        general.append(z.get_text().strip())

        elif i=="Types of care":
            for k in soup.findAll(class_="attribute-group"):
                if k.find(class_='text-body').get_text().strip() == i:
                    for z in k.findAll('li'):
                        typeOfCare.append(z.get_text().strip())
        elif i=="Training Areas":
            for k in soup.findAll(class_="attribute-group"):
                if k.find(class_='text-body').get_text().strip() == i:
                    for z in k.findAll('li'):
                        trainingAreas.append(z.get_text().strip())

        elif i=="Licenses":
            for k in soup.findAll(class_="attribute-group"):
                if k.find(class_='text-body').get_text().strip() == i:
                    for z in k.findAll('li'):
                        licenses.append(z.get_text().strip())



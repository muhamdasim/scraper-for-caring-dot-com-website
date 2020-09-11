import pandas as pd
import caring_scraper as scraper
import csv
urls = []
df = pd.read_csv('urls.csv')
for i in df['urls']:
    urls.append(i)

# list definitions
url=[]
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

counter = 0

for i in urls:
    try:
        soup = scraper.pageRequest(i)
        print("Scraping:", i)
        n=scraper.communityName(soup)
        url.append(i)
        communityName.append(n)
        pageTitle.append(scraper.pageTitle(soup))
        metaDescription.append(scraper.MetaDescription(soup))
        communityStreetAddress.append(scraper.getCommunityStreetAddress(soup))
        communityCity.append(scraper.getCommunityCity(soup))
        communityState.append(scraper.getCommunityState(soup))
        communityZipCode.append(scraper.getCommunityZipCode(soup))
        communityImages.append(scraper.getCommunityImages(soup))
        altTags.append(scraper.getAltTags(soup))
        imageTitle.append(scraper.getImageTitle(soup))
        communityContent.append(scraper.getCommunityContent(soup))
        averageReviewScore.append(scraper.getAverageReviewScore(soup))
        roomHousingOptions.append(scraper.getROOMANDHOUSINGOPTIONS(soup))
    except:
        continue


with open("apfm-data.csv", "w",newline='',encoding="utf-8") as csvFile:
    fieldnames = ['url','pageTitle','metaDescription','communityReviews','communityStreetAddress','communityCity','communityState','communityZipCode','communityImages','communityContent','noOfReviews','averageProfileScore','careTypesProvided','communityAmenities','licenseNo']
    writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
    writer.writeheader()
    for link,pTitle,mDescription,cReviews,cStreetAddress,cCity,cState,cCode,cImages,cContent,nReviews,aScore,cProvided,cAmenities,lNo in zip(url,pageTitle,communityReviews,metaDescription,communityStreetAddress,communityCity,communityState,communityZipCode,communityImages,communityContent,noOfReviews,averageProfileScore,careTypesProvided,communityAmenities,licenseNo):
        writer.writerow({'url':link,'pageTitle':pTitle,'metaDescription':mDescription,'communityReviews':cReviews,'communityStreetAddress':cStreetAddress,'communityCity':cCity,'communityState':cState,'communityZipCode':cCode,'communityImages':cImages,'communityContent':cContent,'noOfReviews':nReviews,'averageProfileScore':aScore,'careTypesProvided':cProvided,'communityAmenities':cAmenities,'licenseNo':lNo})

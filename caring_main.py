import pandas as pd
import caring_scraper as scraper

urls = []
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

counter = 0

for i in urls:
    soup = scraper.pageRequest('https://www.caring.com/senior-living/washington/seattle/merrill-gardens-at-first-hill-98101')
    print("Scraping:", i)
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
    roomHousingOptions.append(scraper.getROOMANDHOUSINGOPTIONS(soup))

    for i in soup.find_all(class_='attribute-group'):
        print(i.find(class_='text-body').get_text().strip())


    costs.append(scraper.getCosts(soup))

    counter += 1
    if counter == 1:
        break



for i in costs:
    print(i)



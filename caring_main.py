import pandas as pd
import caring_scraper as scraper
import csv

urls = []
df = pd.read_csv('urls.csv')
for i in df['urls']:
    urls.append(i)

# list definitions
url = []
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


def saveData():
    print("Data Saved")
    with open("caring-data.csv", "w", newline='', encoding="utf-8") as csvFile:
        fieldnames = ['url', 'pageTitle', 'metaDescription', 'communityName', 'communityStreetAddress', 'communityCity',
                      'communityState', 'communityZipCode', 'communityImages', 'altTags', 'imageTitle',
                      'communityContent', 'averageReviewScore', 'costs', 'roomHousingOptions', 'diningOptions',
                      'features', 'cleaningServices', 'techEntertainment', 'healthServices', 'activities',
                      'financialGuidance', 'guestServices', 'languages', 'general', 'typeOfCare', 'trainingAreas',
                      'licenses']
        writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
        writer.writeheader()
        for link, pT, mD, cN, cSA, cC, cS, cZC, cI, aT, iT, cCo, aRS, c, rHO, dO, f, cSer, tE, hS, a, fG, gS, l, g, tOC, tA, lic in zip(
                url, pageTitle, metaDescription, communityName, communityStreetAddress, communityCity, communityState,
                communityZipCode, communityImages, altTags, imageTitle, communityContent, averageReviewScore, costs,
                roomHousingOptions, diningOptions, features, cleaningServices, techEntertainment, healthServices,
                activities, financialGuidance, guestServices, languagues, general, typeOfCare, trainingAreas, licenses):
            writer.writerow({'url': link, 'pageTitle': pT, 'metaDescription': mD, 'communityName': cN,
                             'communityStreetAddress': cSA, 'communityCity': cC, 'communityState': cS,
                             'communityZipCode': cZC, 'communityImages': cI, 'altTags': aT, 'imageTitle': iT,
                             'communityContent': cCo, 'averageReviewScore': aRS, 'costs': c, 'roomHousingOptions': rHO,
                             'diningOptions': dO, 'features': f, 'cleaningServices': cSer, 'techEntertainment': tE,
                             'healthServices': hS, 'activities': a, 'financialGuidance': fG, 'guestServices': gS,
                             'languages': l, 'general': g, 'typeOfCare': tOC, 'trainingAreas': tA, 'licenses': lic})


for i in urls:
    try:
        soup = scraper.pageRequest(i)
        print("Scraping:", i)
        n = scraper.communityName(soup)
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

        costs.append(scraper.getCosts(soup))
        roomHousingOptions.append(scraper.getROOMANDHOUSINGOPTIONS(soup))
        diningOptions.append(scraper.getDiningOptions(soup))
        features.append(scraper.getFeatures(soup))
        cleaningServices.append(scraper.getCleaningServices(soup))
        techEntertainment.append(scraper.getTechnologyAndEntertainment(soup))
        healthServices.append(scraper.getHealthServices(soup))
        activities.append(scraper.getActivities(soup))
        financialGuidance.append(scraper.getFinancialGuidance(soup))
        guestServices.append(scraper.getGuestServices(soup))
        languagues.append(scraper.getLanguages(soup))
        general.append(scraper.getGeneral(soup))
        typeOfCare.append(scraper.getTypesOfCare(soup))
        trainingAreas.append(scraper.getTrainingAreas(soup))
        licenses.append(scraper.getLicenses(soup))

        counter += 1
        if (counter%10)==1:
            saveData()
    except:
        print("Error",i)
        continue

import requests
from bs4 import BeautifulSoup
from itertools import islice
import json

# list to string

def listToString(s):
    # initialize an empty string
    str1 = " "

    # return string
    return (str1.join(s).strip())


# Requesting Page


def pageRequest(i):
    r = requests.get(i)
    return BeautifulSoup(r.text, 'lxml')


def pageTitle(soup):
    return soup.title.string


def MetaDescription(soup):
    data = soup.find_all('meta')
    return listToString(
        [meta.attrs['content'] for meta in data if 'name' in meta.attrs and meta.attrs['name'] == 'description'])


def communityName(soup):
    return soup.find(itemprop='name').h1.text.strip()


def getCommunityStreetAddress(soup):
    return soup.find(class_='street-address').text.strip() + "," + getCommunityCity(soup) + "," + getCommunityState(
        soup) + getCommunityZipCode(soup)


def getCommunityCity(soup):
    return soup.find(class_='locality').text.strip()


def getCommunityState(soup):
    return soup.find(class_='region').text.strip()


def getCommunityZipCode(soup):
    return soup.find(class_='postal-code').text.strip()


def getCommunityImages(soup):
    data = []
    limit = int(len(soup.find_all(class_='item')) / 2)
    for i in islice(soup.find_all(class_='item'), limit):
        data.append(i.find('img').get('data-src'))
    str=''
    for i in data:
        str += i + " "

    return str[:-1]


def getCommunityContent(soup):
    content = soup.select('#description')
    str=''
    for i in content:
        str+=i.get_text().strip()+' '

    st=str.replace('Is this your business?','')
    return st[:-1]

def getAverageReviewScore(soup):
    return soup.find(class_='count text-title4').text.strip()


def getAltTags(soup):
    limit = int(len(soup.find_all(class_='item')) / 2)
    for i in islice(soup.find_all(class_='item'), limit):
        return i.find('img').get('alt')

def getImageTitle(soup):
    limit = int(len(soup.find_all(class_='item')) / 2)
    for i in islice(soup.find_all(class_='item'), limit):
        return i.find('img').get('title')

def getCosts(soup):
    for i in soup.find_all(class_='attribute-group'):
        if i.find('h4').get_text().strip() == "Costs":
            dt = []
            for j in i.findAll('li'):
                dt.append(j.get_text().strip())
            return (listToString(dt))

    return -1

def getROOMANDHOUSINGOPTIONS(soup):
    for i in soup.find_all(class_='attribute-group'):
        if i.find('h4').get_text().strip() == "Room and housing options":

            dt = []
            for j in i.findAll('li'):
                dt.append(j.get_text().strip())


            return (listToString(dt))


    return -1

def getDiningOptions(soup):
    for i in soup.find_all(class_='attribute-group'):
        if i.find('h4').get_text().strip() == "Dining options":
            dt = []
            for j in i.findAll('li'):
                dt.append(j.get_text().strip())

            return (listToString(dt))


    return -1

def getFeatures(soup):
    for i in soup.find_all(class_='attribute-group'):
        if i.find('h4').get_text().strip() == "Features":
            dt = []
            for j in i.findAll('li'):
                dt.append(j.get_text().strip())

            return (listToString(dt))


    return -1

def getCleaningServices(soup):
    for i in soup.find_all(class_='attribute-group'):
        if i.find('h4').get_text().strip() == "Cleaning services":
            dt = []
            for j in i.findAll('li'):
                dt.append(j.get_text().strip())

            return (listToString(dt))


    return -1

def getTechnologyAndEntertainment(soup):
    for i in soup.find_all(class_='attribute-group'):
        if i.find('h4').get_text().strip() == "Technology and entertainment":
            dt = []
            for j in i.findAll('li'):
                dt.append(j.get_text().strip())

            return (listToString(dt))


    return -1

def getHealthServices(soup):
    for i in soup.find_all(class_='attribute-group'):
        if i.find('h4').get_text().strip() == "Health services":
            dt = []
            for j in i.findAll('li'):
                dt.append(j.get_text().strip())

            return (listToString(dt))


    return -1

def getActivities(soup):
    for i in soup.find_all(class_='attribute-group'):
        if i.find('h4').get_text().strip() == "Activities":
            dt = []
            for j in i.findAll('li'):
                dt.append(j.get_text().strip())

            return (listToString(dt))


    return -1

def getFinancialGuidance(soup):
    for i in soup.find_all(class_='attribute-group'):
        if i.find('h4').get_text().strip() == "Financial guidance":
            dt = []
            for j in i.findAll('li'):
                dt.append(j.get_text().strip())

            return (listToString(dt))


    return -1

def getGuestServices(soup):
    for i in soup.find_all(class_='attribute-group'):
        if i.find('h4').get_text().strip() == "Guest services":
            dt = []
            for j in i.findAll('li'):
                dt.append(j.get_text().strip())

            return (listToString(dt))


    return -1

def getLanguages(soup):
    for i in soup.find_all(class_='attribute-group'):
        if i.find('h4').get_text().strip() == "Languages":
            dt = []
            for j in i.findAll('li'):
                dt.append(j.get_text().strip())

            return (listToString(dt))


    return -1

def getGeneral(soup):
    for i in soup.find_all(class_='attribute-group'):
        if i.find('h4').get_text().strip() == "General":
            dt = []
            for j in i.findAll('li'):
                dt.append(j.get_text().strip())

            return (listToString(dt))


    return -1

def getTypesOfCare(soup):
    for i in soup.find_all(class_='attribute-group'):
        if i.find('h4').get_text().strip() == "Types of care":
            dt = []
            for j in i.findAll('li'):
                dt.append(j.get_text().strip())

            return (listToString(dt))

    return -1

def getTrainingAreas(soup):
    for i in soup.find_all(class_='attribute-group'):
        if i.find('h4').get_text().strip() == "Training Areas":
            dt = []
            for j in i.findAll('li'):
                dt.append(j.get_text().strip())

            return (listToString(dt))


    return -1

def getLicenses(soup):
    for i in soup.find_all(class_='attribute-group'):
        if i.find('h4').get_text().strip() == "Licenses":
            dt = []
            for j in i.findAll('li'):
                dt.append(j.get_text().strip())

            return (listToString(dt))


    return -1

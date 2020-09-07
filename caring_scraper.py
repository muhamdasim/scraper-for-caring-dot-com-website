import requests
from bs4 import BeautifulSoup
from itertools import islice


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

    for i in data:
        data += i + ","

    return data[:-1]


def getCommunityContent(soup):
    content = soup.find('div', class_='section-content').get_text().strip()
    print(content)


def test(soup):
    return 0

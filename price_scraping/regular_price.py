import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import numpy
from urllib.parse import urlsplit
import requests

def get_skins_url_per_champion(sitemap_skin_url : str = "https://www.mobafire.com/sitemap-skins.xml"):
    liste_url_per_champion = []
    response = requests.get(sitemap_skin_url)
    xml = BeautifulSoup(response.text)
    urls = xml.find_all('url')
    for url in urls:
        if xml.find('loc'):
            loc = url.findNext('loc').text
            liste_url_per_champion.append(loc)
    return liste_url_per_champion

def get_skins_prices_for_champion(champion_url : str):
    dict_skins = {}
    response = requests.get(champion_url)
    page = BeautifulSoup(response.text, 'html.parser')
    divs = page.find_all('div', {"class" : "view-skin"})
    for div in divs:
        name_div = div.find('div', {"class" : "view-skin__image__meta__left"})
        if name_div:
            name = name_div.find('h2').string
            price_div = div.find('div', {"class" : "champ-skins__item__cost tablet-up"})
            if price_div:
                price = price_div.string
            else:
                price = "Unknown"
            dict_skins[name] = price
    return dict_skins


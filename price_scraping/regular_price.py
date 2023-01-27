import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import numpy
from urllib.parse import urlsplit
import requests
import json

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
    name_champion = champion_url.rsplit('/', 1)[-1]
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
    return name_champion, dict_skins

def get_skins_prices_all(liste_url_per_champion):
    final_dict = {}
    for url_champion in liste_url_per_champion:
        name_champion, dict_champion = get_skins_prices_for_champion(champion_url = url_champion)
        final_dict[name_champion] = dict_champion
        print(f"{name_champion} : Done")
    return final_dict

def export_dict_to_json(file_path : str, my_dict : dict):
    with open(file_path, "w", encoding='utf8') as outfile:
        json.dump(my_dict, outfile)
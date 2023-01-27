import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import numpy
from urllib.parse import urlsplit
import requests
import json

def get_sales(url_dote_page : str = "https://dotesports.com/league-of-legends/news/league-of-legends-weekly-champion-and-skin-sale"):
    response = requests.get(url_dote_page)
    page = BeautifulSoup(response.text)
    main_content = page.find('div', {"class" : "entry-content"})
    skins = main_content.find(id="skins")
    lines_after_skins = skins.find_next_siblings()
    cont = []
    new_dict = {}
    for line in lines_after_skins:
        line_soup = BeautifulSoup(str(line), 'html.parser')
        tag = line_soup.find("h3")
        if tag:
            string_content = tag.text
            cont.append(tag.text)
            skin_name = string_content[:string_content.find(":")]
            price = (string_content.split(" RP")[0].split(":")[-1])[1:]
            percentage = (string_content.split(" percent")[0].split(" ")[-1])[1:]
            temp_dict = {}
            temp_dict['price'] = price
            temp_dict['percentage'] = percentage
            new_dict[skin_name] = temp_dict
    return new_dict
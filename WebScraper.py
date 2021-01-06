import requests
import random
from bs4 import BeautifulSoup
from urllib.request import urlopen 

def top100games():
    url = 'https://store.steampowered.com/stats/'  
    page = requests.get(url)
    html = page.text
    soup = BeautifulSoup(html, "html.parser")
    anchor = soup.findAll('a', attrs={'class': 'gameLink'})
    newString = ""
    for i in anchor:
        newString = newString + i.text + "\n"
    return newString
import requests
import urllib.request
import time
import json
from bs4 import BeautifulSoup
import helpers

url = 'https://www.revelstokemountainresort.com/conditions/snow-report'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
snowreport = soup.findAll('section')

temperatures = helpers.getTemperatures(soup)
newSnow = helpers.getNewSnow(soup)
wind = helpers.getWind(soup)
base = helpers.getBase(soup)
dateUpdated = helpers.getLastUpdatedDate(soup)

data = {
    "temperatures": temperatures,
    "freshSnow": newSnow,
    "wind": wind,
    "base": base,
    "dateUpdated": dateUpdated
}

with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)
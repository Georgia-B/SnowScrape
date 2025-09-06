import requests
import urllib.request
import time
import json
from bs4 import BeautifulSoup
import helpers
import asyncio
from playwright.async_api import async_playwright
from datetime import datetime

async def main():
    url = 'https://www.revelstokemountainresort.com/mountain/conditions/snow-report'
    # response = requests.get(url)
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)
        await page.wait_for_event("response", lambda response: 'snow-weather-json' in response.url and response.status == 200)
        html = await page.content()
        await browser.close()


    soup = BeautifulSoup(html, "html.parser")
    snowreport = soup.find_all('section')

    temperatures = helpers.getTemperatures(soup)
    wind = helpers.getWind(soup)
    snow = helpers.getSnow(soup)
    date = datetime.now().strftime("%d %B %Y, %I:%M %p")
    dateUpdated = {
        "title": "Last updated",
        "date": date
    }    

    data = {
        "temperatures": temperatures,
        "wind": wind,
        "snow": snow,
        "dateUpdated": dateUpdated
    }
    print(data)

    with open('data.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)


if __name__ == "__main__":
    asyncio.run(main())
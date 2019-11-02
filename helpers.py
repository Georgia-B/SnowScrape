def getTemperatures(document):
    tempList = []
    temperatures = document.find('div', {"class": "temperatures"}).findAll('div', {"class": "four columns alpha"})
    for temp in temperatures:
        titles = temp.find('span').findChildren()
        title = titles[0].text
        subtitle = titles[1].text

        celcius = temp.findAll('strong')[1].text
        fahrenheit = temp.findAll('small')[1].text

        tempDict = {
            "title": title,
            "subtitle": subtitle,
            "celcius": celcius,
            "fahrenheit": fahrenheit
        }
        tempList.append(tempDict)
    return tempList

def getNewSnow(document):
    newsnow = document.find('div', {"class": "new-snow"})
    snowCms = newsnow.findAll('strong')[1].text

    snow = {
        "title": "Fresh snow",
        "cms": snowCms,
    }
    return snow

def getWind(document):
    wind = document.find('div', {"class": "wind"}).findChild()
    title = wind.find('span').findChild().text
    value = wind.contents[2].strip()
    windDict = {
        "title": title,
        "value": value
    }
    return windDict

def getBase(document):
    base = document.find('div', {"class": "four columns center border-box border-right"}).findChild()
    title = base.find('span').findChild().text
    value = base.findAll('strong')[1].text
    baseDict = {
        "title": title,
        "value": value
    }
    return baseDict

def getLastUpdatedDate(document):
    lastUpdated = document.find('p', {"class": "eight columns omega text-right"})
    date = lastUpdated.find('strong').text
    dateObj = {
        "title": "Date updated",
        "date": date
    }
    return dateObj
    
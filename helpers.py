def getTemperatures(document):
    conditions = document.find_all('div', {"class": "condition__text"})
    temperatureList = []
    for condition in conditions:
        if condition.find('span', {"data-wsid": "temperature"}):
            title = condition.find("dt", {"class": "condition__term"}).text
            titleParts = title.split('(')
            label=titleParts[0].strip().title()
            elevation= titleParts[1].replace(')','').strip().lower()
            value = condition.find('span', {"data-wsid": "temperature"}).text.strip()

            tempObj = {
                "label": label,
                "elevation": elevation,
                "value": value,
            }
            temperatureList.append(tempObj)
    
    return temperatureList

def getSnow(document):
    allSnowAmounts = document.find_all('div', { "class": "snow-report__amount"})
    lastHour = {}
    last24Hours = {}
    base = {}
    for amount in allSnowAmounts:
        title = amount.find('h2', {"class": "snow-report__title"}).text.lower()
        value = amount.find('span', { "class": "value"}).text
        if title == "last hour":
            lastHour = {
                "title": "Last hour",
                "value": value
            }
        if title == "24 hours":
            last24Hours = {
                "title": "24 hours",
                "value": value
            }
        if title == "base depth":
            base = {
                "title": "Base depth",
                "value": value
            }
    return {
        "lastHour": lastHour,
        "last24Hours": last24Hours,
        "base": base
    }

def getWind(document):
    conditions = document.find_all('div', {"class": "condition__text"})
    windObj = {}
    for condition in conditions:
        if condition.find('span', {"data-wsid": "wind"}):
            direction = condition.find("span", {"data-wsid": "direction"}).text
            value = condition.find('span', {"data-wsid": "wind"}).text.strip()

            windObj = {
                "label": "Wind speed",
                "direction": direction,
                "value": value,
            }
    return windObj

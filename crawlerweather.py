import requests
from bs4 import BeautifulSoup
from countiesandcities import *
import pandas as pd
import re

def the_weather(location):
    url = "https://weather.com/zh-TW/weather/5day/l/" + taiwan[location]
    response = requests.get(url)

    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find(id='twc-scrollabe').table.tbody

    rows = table.find_all('tr')

    rain = []

    tmp = []
    tmp2 = []

    hum = []
    hum2 = []

    dr = re.compile(r'<[^>]+>',re.S)

    for r in rows:
        precip = r.find('td', 'precip').div.find('span', '').span.text
        precip_result = precip.split('%')[0]
        rain.append(precip_result)

    for b in rows:
        temp = b.find('td', 'temp').div.find_all('span', '')
        tmp.append(temp)

    for f in rows:
        humidity = f.find('td', 'humidity').find('span', '')
        hum.append(humidity)

    def insert_str(string, str_to_insert, index):
        return string[:index] + str_to_insert + string[index:]

    for a in range(3):
        dd = dr.sub('', str(hum[a]))
        cleanString = re.sub('\W+', '', dd)
        hum2.append(cleanString)

    for i in range(3):
        dd = dr.sub('', str(tmp[i]))
        cleanString = re.sub('\W+', '', dd)
        tmp2.append(cleanString)

        for i in range(len(tmp2)):
            if len(tmp2[i]) == 4:
                tmp2[i]=insert_str(tmp2[i], "/", 2)


    times = ["Today","tomorrow","AF tomorrow"]

    pd.set_option('display.unicode.ambiguous_as_wide', True)
    pd.set_option('display.unicode.east_asian_width', True)

    # df = pd.DataFrame(list(zip(times, tmp2, rain[:3], hum2)),
    #                columns =['時間', '氣溫 高/低', '降雨機率', '濕度'])

    from tabulate import tabulate

    df = pd.DataFrame({'time' : times,
                       'tmp H/L' : tmp2,
                       'rain%': rain[:3],
                       'humidity': hum2
                       })

    return df.to_string(index=False, justify='right')
# telegram-taiwan-weather-forecasting-bot

A telegram bot that will tell you the weather forecast for counties and cities in Taiwan for the next 3 days including: temperature, humidity and rainfall rate

### Prerequisites

Telegram Desktop : https://desktop.telegram.org/
Telegram Botfather : https://www.youtube.com/watch?v=bmOW3LpNfbs

### Installing

What things you need to install

```
pip install pandas
pip install BeautifulSoup4
pip install requests
```

## How to Run

Please copy and paste your bot token to the main.py 
```
Updater('token') 
```

notes: the weather message parse_mode is base on the html style, so the text could be missing order when you show on the mobile device.

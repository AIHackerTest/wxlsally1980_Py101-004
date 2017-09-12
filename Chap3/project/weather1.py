# -*- coding: utf-8 -*-
import requests

def fetch_weather(location):
    result = requests.get('https://api.seniverse.com/v3/weather/now.json', params={
                'key': 'bikdwteu8tiybqtt',
                'location':location,
                'language': 'zh-cn'
        }, timeout=10)
    result_get = result.json()  
    weather = result_get['results'][0]['now']['text']
    temperature = result_get['results'][0]['now']['temperature']
    #last_update = result.json().get('results')[0]['last_update']
    weather_str = location + '此刻的天气是：' + str(weather) + ',气温' + str(temperature) + '度。'
    return weather_str
    
    
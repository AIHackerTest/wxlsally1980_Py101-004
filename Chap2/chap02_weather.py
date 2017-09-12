#-*- coding: UTF-8 -*-   

from sys import exit


# 读取文件，将内容存入列表
with open('/Users/wuxiaoli/hardway/thinkpage_cities_English_name.txt', encoding="utf-8")as f:
    cities = []
    for line in f.read( ).split('\n'):
        cities.append(line)


history_info = ""


while True:
    print('请输入城市名称查询天气，如果需要帮助，请输入help或者问号。')
    user_input = input('请输入指令:')
    if user_input in cities:
        import requests
        r = requests.get(('https://api.seniverse.com/v3/weather/now.json?key=bikdwteu8tiybqtt&location=%s&language=zh-Hans&unit=c')% user_input)
        weather = r.json()
        s = weather['results'][0]['now']['text']
        print ("天气:", s)
        t = weather['results'][0]['now']['temperature']
        print ("温度:", t)
        history_data = user_input + ',' + "天气:", s + "温度:", t + '\n'
        history_info = history_info + history_data
    elif user_input == 'history':
        print (history_info)
    elif user_input == 'help' or user_input == '?':
        print ('输入城市名，查询该城市的天气；')
        print ('输入 help，获取帮助文档；')
        print ('输入 history，获取查询历史；')
        print ('输入 quit，退出天气查询系统。')
    elif user_input == 'quit' or user_input == 'q':
        print ('退出程序，欢迎下次使用。')
        print (history_info)
        exit()
    else:
        print ('您的查询不成功，可能是因为没有您要查询的城市的天气状况信息。')    



  

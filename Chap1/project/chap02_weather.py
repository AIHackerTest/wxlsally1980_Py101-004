#-*- coding: UTF-8 -*-   

from sys import exit

weather_dic = {}


# 读取文件，将内容存入字典
with open('/Users/wuxiaoli/hardway/weather_info.txt') as file:
    for info in file.readlines():
        city = info.split(',')[0]
        weather = info.split(',')[1].rstrip('\n')
        weather_dic[city] = weather
history_info = ""

while True:
    print('请输入城市名称查询天气，如果需要帮助，请输入help或者问号。')
    user_input = input('请输入指令:')
    if user_input in weather_dic:
        print (user_input, '的天气状况为:', weather_dic[user_input])
        history_data = user_input + ',' + weather_dic[user_input] + '\n'
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

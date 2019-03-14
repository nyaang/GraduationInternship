# -*- coding: utf-8 -*-
import pandas as pd 
from urllib.request import urlopen, quote
import json

house = pd.read_csv('./58.csv', encoding='gbk')

url = 'http://api.map.baidu.com/geocoder/v2/'
ak = 'b06GtnG4uK5U88Xdcx7Ul0QUd3smrtv5'

for i in range(house.shape[0]):

    #print(house['区域'][i].strip(),house['次级区域'][i].strip(),house['详细地址'][i].strip(),house['小区名'][i].strip())
    city = "北京市"+house['区域'][i].strip()+house['次级区域'][i].strip()+house['详细地址'][i].strip()+house['小区名'][i].strip()
    #print(address)
    price = house['价格'][i]
    #print(address+str(price))

    #转换格式
    add = quote(city)
    # 以 json 的格式输出
    output = 'json'
    # URL 正式拼接，这一句画，下面还会详解解释
    uri = url + '?' + 'address=' + add + '&output=' + output + '&ak=' + ak
    #print(uri)
    req = urlopen(uri)
    # 传入的字符串,需要解码
    res = req.read().decode()
    # 写成json形式，
    temp = json.loads(res)

    # 经度
    lng = temp['result']['location']['lng']
    #纬度
    lat = temp['result']['location']['lat']
    str_temp = '{"lat":' + str(lat) + ',"lng":' + str(lng) + ',"count":' + str(price) +'},'
    #print(str_temp)
    with open('./jingweidu.txt','a') as f:
        f.write(str_temp)
        f.write('\n')

'''
@Author: Wang Meng
@Date: 2020-06-26 13:22:43
@LastEditors: Wang Meng
@LastEditTime: 2020-06-27 16:00:27
@Description: https://www.back4app.com/database/back4app/list-of-all-continents-countries-cities
'''
import json
import urllib
import requests


headers = {
    # This is your app's application id
    'X-Parse-Application-Id': '****************************************',
    # This is your app's REST API key
    'X-Parse-REST-API-Key': '****************************************'
}

# access to overseas
proxy = '127.0.0.1:1087'
proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
}

# used to download small datasets
url = 'https://parseapi.back4app.com/classes/Continentscountriescities_Continent?limit=10&order=name'
# url = 'https://parseapi.back4app.com/classes/Continentscountriescities_Language?limit=1000&order=code'
# url = 'https://parseapi.back4app.com/classes/Continentscountriescities_Subdivisions_States_Provinces?limit=5000'
# url = 'https://parseapi.back4app.com/classes/Continentscountriescities_Country?limit=1000&order=name'

data = json.loads(requests.get(url, headers=headers, proxies=proxies).content.decode('utf-8'))  # Here you have the data that you need
with open("Continents.json", "w") as fo:
    for record in data["results"]:
        fo.write(json.dumps(record, ensure_ascii=False) + "\n")

# used to download cities data, number of cities equals 1362963
# with open("Cities6.json", "a") as fo:
#     skip = 0
#     while skip < 137:
#         url = 'https://parseapi.back4app.com/classes/Continentscountriescities_City?skip=' + str(skip * 10000) + '&limit=10000&order=country'
#         # url = 'https://parseapi.back4app.com/classes/Continentscountriescities_City?skip=' + \
#         #     str(959999) + '&limit=1&order=country'
#         skip += 1
#         data = json.loads(requests.get(url, headers=headers, proxies=proxies).content.decode(
#             'utf-8'))  # Here you have the data that you need
#         # print(json.dumps(data, indent = 2))
#         for record in data["results"]:
#             fo.write(json.dumps(record, ensure_ascii=False) + "\n")
#         # break

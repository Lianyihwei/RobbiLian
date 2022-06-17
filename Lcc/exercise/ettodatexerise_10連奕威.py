import requests
from bs4 import BeautifulSoup
import pandas as pd

# 練習一，輸入要查詢的城市名稱爬取title及url
# 要爬的url跟input結合
city = input("請輸入要查詢旅遊資料:")
url =" https://travel.ettoday.net/category/"+city+"/"
res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")
title_url_tag = ".box_0 h3 a"
title_urls = soup.select(title_url_tag)
# 建空list存解析後的title跟url
title = []
urls = []
for i in title_urls:
    title.append(i.text)
    urls.append(i.get("href"))
# 將title跟url合併成字典帶入pandas
data = {"Title":title,"Url":url}
df = pd.DataFrame(data)

# 練習二，把所以城市的旅遊資料一次爬下
# 先爬所有城市的名稱並存入city_list
# url = "https://travel.ettoday.net/"
# res = requests.get(url)
# soup = BeautifulSoup(res.text, "lxml")
# categorys = soup.select("ul.clearfix li div")
# # 整理爬下的city_list資料
# # 先用\n分隔字串
# # 再將空字串去掉
# city_list = categorys[2].get_text().split("\n")
# city_list = [x for x in city_list if x!=""]
# cities = []
# titles= []
# urls = []
# # 再將得到的城市名稱用迴圈一一取出title跟url存入字典 
# for city in city_list:
#     url = "https://travel.ettoday.net/category/"+city+"/"
#     res = requests.get(url)
#     soup = BeautifulSoup(res.text, "lxml")
#     title_url_tag = ".box_0 h3 a"
#     title_urls = soup.select(title_url_tag)
#     for i in title_urls:
#         cities.append(city)
#         titles.append(i.text)
#         urls.append(i.get("href"))
# all_cities_data = {"City":cities,"Title":titles,"Url":urls}
# df = pd.DataFrame(data)
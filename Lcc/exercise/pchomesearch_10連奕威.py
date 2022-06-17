from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import lxml

# pchome爬搜尋商品結果的title跟url，pchome每頁不會載入20筆資料
# 方法一，用selenium搭配拉滾動條往頁底滑載多更多筆數

browser = webdriver.Chrome()
url = "https://shopping.pchome.com.tw/"
browser.implicitly_wait(5)
browser.get(url)
browser.find_element_by_id("keyword").send_keys("iphone")
browser.find_element_by_id("doSearch").click()
for i in range(3):
    print("slide {}".format(i) )
    js = "var action=document.documentElement.scrollTop=1000000"
    browser.execute_script(js)
soup = BeautifulSoup(browser.page_source, "lxml")
results_tag = "h5 a"
results = soup.select(results_tag)
browser.quit()
title = []
url = []
data = {}
for result in results:
    title.append(result.text)
    url.append(result.get("href"))
data = {"Title": title, "Url": url}
df = pd.DataFrame(data)


# 方法二，用requests方式搭配json解析結果
# import pandas as pd
# import requests
# import json
# import time
# product = input("請輸入要查詢的商品:")
# pages = int(input("請輸入要查詢的頁數:"))
# titles = []
# urls = []
# data = {}
# for page in range(1, pages+1, 1):
#     url = "https://ecshweb.pchome.com.tw/search/v3.3/all/results?q="+product+"&page="+str(page)+"&sort=sale/dc"
#     res = requests.get(url)
#     json_data = json.loads(res.content)
#     time.sleep(2)
#     for i in range(20):
#         titles.append(json_data["prods"][i]["name"])
#         urls.append("https://24h.pchome.com.tw/prod/"+json_data["prods"][i]["Id"])
# data = {"Title": titles, "Url": urls}
# df = pd.DataFrame(data)

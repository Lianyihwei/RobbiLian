from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import lxml

browser = webdriver.Chrome()
url = "https://shopping.pchome.com.tw/"
time.sleep(3)
browser.get(url)
browser.find_element_by_id("keyword").send_keys("iphone")
browser.find_element_by_id("doSearch").click()
time.sleep(3)
new_url = browser.current_url
browser.get(new_url)
time.sleep(3)
for i in range(3):
    print("slide {}".format(i) )
    js = "var action=document.documentElement.scrollTop=1000000"
    browser.execute_script(js)
    time.sleep(2)
soup = BeautifulSoup(browser.page_source, "lxml")
results_tag = "h5 a"
results = soup.select(results_tag)
print(len(results))
browser.quit()
# browser.implicitly_wait(5)
# browser.quit()

# soup = BeautifulSoup(browser.page_source, "html.parse")
# results_tag = "h5 a"
# results = soup.select(results_tag)
# for r in results:
#     print(r.text)
#     print(r.get("href"))
# browser=webdriver.Chrome()
# browser.get("https://www.w3schools.com/")
# target  = browser.find_element(By.LINK_TEXT, "BROWSE TEMPLATES")
# # browser.execute_script("arguments[0].scrollIntoView(true);",target)
# target.location_once_scrolled_into_view
# time.sleep(2)
# browser.quit()
# print("success")

# url =" https://travel.ettoday.net/category/"+"台北"+"/"
# print(url)

# url = 'https://tw.yahoo.com/'
# browser = webdriver.Chrome()
# browser.get(url)
# find_data=browser.find_element_by_id('header-search-input')
# find_data.send_keys('topgun')
# sumbit=browser.find_element_by_id('header-desktop-search-button').click()

# browser=webdriver.Chrome() #開啟模擬瀏覽器
# browser.get("https://www.google.com/")
# element = browser.find_element_by_name("q")
# element.send_keys("捍衛戰士2")
# element.submit()
# results = browser.find_elements_by_css_selector(".yuRUbf a")
# google_titles = []
# google_urls = []
# for title in results:
#     google_titles.append(title.text())
# for url in results:
#     google_urls.append(url.get_attribute("href"))
# browser.quit() # 關閉瀏覽器
# print("Titles: ", google_titles)
# print("urls:", google_urls)
# browser.quit()

# browser=webdriver.Chrome() #開啟模擬瀏覽器
# browser.get("https://www.bing.com/")
# element = browser.find_element_by_id("sb_form_q")
# element.send_keys("捍衛戰士2")
# element.submit()
# results = browser.find_elements_by_css_selector(".b_algo a")
# bing_titles = []
# bing_urls = []
# for title in results:
#     bing_titles.append(title.text)
#     bing_urls.append(title.get_attribute("href"))
# browser.quit() # 關閉瀏覽器

# print("Titles: ", bing_titles,"\n")
# print("Urls:", bing_urls)

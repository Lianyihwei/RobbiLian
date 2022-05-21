"""
yfinance方法中取到的info資訊取出來翻譯
"""
# yfinance ->取得yfinance資料
# googletrans ->翻譯用
# csv ->將結果存成csv檔
from asyncore import write
from requests import head
import yfinance as yf
from googletrans import Translator
import csv

# 用NVDA做範例，yf.Ticker().info可以取得NVDA的基本資料（class,dict）
nvda = yf.Ticker("NVDA")
# 將info的key值轉成list準備帶入googletrans使用
yf_info = list(nvda.info)
# 初始化googletrans.Translator函數，並建一個空list準備接翻譯後的output
trans = Translator()
yf_info_trans_list = []
# 利用迴圈，將info-keylist一個個帶進trans.translate("str",dest="zh-tw")
# 結果存入變數yf_info_trans，再一一append進yf_info_trans_list
for i in range(len(yf_info)):
    yf_info_trans = trans.translate(yf_info[i],dest="zh-tw").text
    yf_info_trans_list.append(yf_info_trans)

# 用dict(zip(lista,listb))將英文info與翻訪後info存成字典後，再轉存成csv檔
yf_info_transdict = dict(zip(yf_info,yf_info_trans_list))
yf_info_transdict

with open("yf_info.csv", "w") as f:
    writer = csv.writer(f)
    for k, v in yf_info_transdict.items():
        writer.writerow([k, v])
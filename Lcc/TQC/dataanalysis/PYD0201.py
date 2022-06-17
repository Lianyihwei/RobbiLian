'''
請撰寫一程式，爬取http://tqc.codejudger.com:3000/target/5201.html，程式須回傳下列資訊：
讓使用者輸入欲搜尋的字詞，再輸出字詞的搜尋結果及字詞出現的次數。
範例輸出
請輸入欲搜尋的字串 : TQC+
TQC+ 搜尋成功
TQC+ 出現 23 次
'''
# 載入模組
import requests
import re

url = 'http://tqc.codejudger.com:3000/target/5201.html'

# 使用 GET 請求
htmlfile = requests.get(url)
# 驗證HTTP Status Code
if htmlfile.status_code == 200:
    # 欲搜尋的字串
    key = input("請輸入欲搜尋的字串 : ")
    check = re.findall(key, htmlfile.text)
    if key in htmlfile.text:
        print(key, "搜尋成功")
        print(key, "出現 %d 次" % len(check))
    else:
        print(key, "搜尋失敗")
        print(key, "出現 0 次")
else:
    print("網頁下載失敗")

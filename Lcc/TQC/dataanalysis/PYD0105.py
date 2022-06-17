'''
請撰寫一程式連結read.db資料庫，
讀取Employee資料表，輸出Employee資料表內的資料。
'''
# 載入 sqlite3 模組
import sqlite3
# 建立資料庫連結
con = sqlite3.connect('read.db')
# 建立cursor物件
datas = con.cursor()

# 查詢Employee資料表
datas.execute("SELECT * FROM Employee")

# 印出查詢結果
for data in datas:
    print(data)

# 關閉與資料庫的連結
con.close()

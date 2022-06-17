'''
請撰寫一程式，讀取文化部展覽資訊read.json，
請將其中title（活動名稱）、showUnit（演出單位）、
startDate（活動起始日期）、endDate（活動結束日期）
等四個欄位內容轉存為write.csv (需為UTF-8編碼格式)，
各欄位內容之間以一個半形逗號隔開。
提示：只需要輸出資料，不需要輸出欄位名稱。
'''

# 載入 json 與 csv 模組
import json
import csv
# 讀取 json 檔案並指定編碼為 utf8
with open("read.json", encoding='utf-8') as file:
    data = json.load(file)

# 寫入 csv 檔案並指定編碼為 utf8
with open("write.csv", "w", encoding='utf-8') as file:
    csv_file = csv.writer(file)
    # 寫入 title（活動名稱）、showUnit（演出單位）、startDate（活動起始日期）、endDate（活動結束日期）等四個欄位
    for item in data:
        csv_file.writerow([item['title'], item['showUnit'],
                        item['startDate'], item['endDate']])

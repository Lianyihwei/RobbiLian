'''
請將其中sno（站點代號）、sna（中文場站名稱）、
tot（場站總停車格）等三個欄位轉存為write.csv (需為UTF-8編碼格式)，
各欄位內容之間以一個半形逗號隔開。
請撰寫一程式，讀取新北市公共自行車即時資訊read.xml，
提示：只需要輸出資料，不需要輸出欄位名稱。
'''
# 載入 xml.etree.ElementTree 模組並縮寫為 ET
import xml.etree.ElementTree as ET
# 載入 csv 模組
import csv
# 讀取 xml
tree = ET.parse("read.xml")
root = tree.getroot()

# 寫入 csv 檔案，編碼設定為 utf8
ubikefile = open("write.csv", "w", encoding='utf-8')
csvwriter = csv.writer(ubikefile)

# 將其中 sno（站點代號）、sna（中文場站名稱）、tot（場站總停車格）等三個欄位寫出
for row in root:
    ubike = []
    sno = row.find('sno').text
    ubike.append(sno)
    sna = row.find('sna').text
    ubike.append(sna)
    tot = row.find('tot').text
    ubike.append(tot)
    csvwriter.writerow(ubike)
ubikefile.close()

# """
# 設變數input、output為接原資料檔input.csv與準備產出的新檔output.csv
# 再讀取input資料，將原資料的內容存在list_input中
# 使用"w"方式依題目要求寫入新資料後，存成新檔output.csv
# """

import csv

input = "input.csv"

with open(input, encoding='utf-8') as f:
    input_file = csv.reader(f)
    list_input = list(input_file)
    f.close()

with open("output.csv","w",newline="", encoding='utf-8') as f:
    output_file = csv.writer(f)
    for row in list_input:
        output_file.writerow(row)
    output_file.writerow(["-----------","-----------"])
    for row in list_input[1:-1]:
        output_file.writerow(row)
    output_file.writerow(["花茶",15])
    output_file.writerow(["蜜荼",10])
    output_file.writerow(["青荼",10])
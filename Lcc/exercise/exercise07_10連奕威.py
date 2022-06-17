import json

data = "/Users/lianyiwei/Documents/python/vscode/poetry-demo/RobbiLian/Lcc/exercise/drugstore.json"

with open(data) as jsdata:
    datas = json.load(jsdata)
drugstore = []
for data in datas:
    if data[0]["機構狀態"] == '開業' and data[2]['地址縣市別'] == '新北市':
            drugstore.append(data)
#     print(f"{drugstore[i][1]['機構名稱']}\t{drugstore[i][2]['地址縣市別']}{drugstore[i][3]['地址鄉鎮市區']}{drugstore[i][4]['地址街道巷弄號']}")
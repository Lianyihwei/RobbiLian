'''
請撰寫一程式，讀取勞保投保薪資分級表read.json內的資料後，
將資料轉存為write.yaml。
3. 輸入輸出：
輸入說明讀取read.json
輸出說明將資料輸出至write.yaml
'''
# 載入 yaml 與 json 模組
import yaml
import json
print(dir(json))
# 讀取 json 檔案
with open("read.json", encoding='utf-8-sig') as file:
    data = json.loads(file)

# 寫入 yaml 檔案
with open("write.yaml", "w", encoding="utf-8") as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True)

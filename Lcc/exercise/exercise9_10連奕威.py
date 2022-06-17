# 建立數據並依照題目要求輸出
import pandas as pd
print(dir(pd))
pd.set_option('display.max_columns',None)

raw_data = {"name": ['小林','小黃','小陳','小美'],
                    "國語":[75,91,71,69],
                    "數學":[62,53,88,53],
                    "英文":[85,56,51,87],
                    "自然":[73,63,69,74],
                    "社會":[60,65,87,70]
                    }
df = pd.DataFrame(raw_data)
df.set_index("name",inplace=True)
print("全部學生成績：\n",df)
print("最後2位學生成績：\n",df.iloc[-2:])
print("以自然遞減排度：\n",df.sort_values("自然",ascending=False)["自然"])
print("第1,3位學生數學自然成績:\n",df[["數學","自然"]][0:3:2])
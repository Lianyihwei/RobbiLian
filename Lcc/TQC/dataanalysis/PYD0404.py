'''
請讀取read.csv中的資料，再以matplotlib輸出長條圖chart.png，
輸出圖表的參數如下：

圖表標題：Score ranges count
X軸名稱：Range
Y軸名稱：Quantity
標題字型大小：20
X軸和Y軸字型大小：14
長條寬度：2
X軸刻度：0~19, 20~39, 40~59, 60~79, 80~100
Y軸刻度：0到25，間隔5
'''
# --開始--批改評分使用，請勿變動
import matplotlib as mpl
mpl.use('Agg')
# --結束--批改評分使用，請勿變動

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# 讀取學生分數資料
# 讀取 read.csv
df = pd.read_csv('read.csv')
scores = df["scores"].values

# range_count[0]: range0~19
# range_count[1]: range20~39
# range_count[2]: range40~59
# range_count[3]: range60~79
# range_count[4]: range80~100
# 以0初始化計數串列
range_count = [0] * 5

# 計數過程
for score in scores:
    if score < 20:
        range_count[0] += 1
    elif score < 40:
        range_count[1] += 1
    elif score < 60:
        range_count[2] += 1
    elif score < 80:
        range_count[3] += 1
    else:
        range_count[4] += 1

# y軸標籤
index = np.arange(0, 25, 5)
# X軸刻度
labels = ['0~19', '20~39', '40~59', '60~79', '80~100']
# 畫出長條圖
plt.bar(index, range_count, width=2)
# 設定X軸名稱
plt.xlabel('Range', fontsize=14)
# 設定Y軸名稱
plt.ylabel('Quantity', fontsize=14)
# 設定x軸標籤
plt.xticks(index, labels)
# 設定y軸標籤
plt.yticks(index)
# 設定圖名稱
plt.title('Score ranges count', fontsize=20)
# 輸出圖片檔案
plt.savefig('chart.png')
plt.close()

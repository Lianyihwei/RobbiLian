'''
依下列要求以matplotlib輸出四個月份（labels = 'Jun', 'Jul', 'Aug', 'Sep'）
的統計圖形chart.png，輸出圖表的參數如下：

完成左右兩個圖，左圖為長條圖（bar），右圖為圓餅圖（pie）
長條圖以labels為X軸，sizes為Y軸，各長條顏色為藍色（blue）
圓餅圖以labels為圖標，sizes為各項所占百分比
圓餅圖colors為各項顏色，長寬比為1:1，並突顯「Aug」
圓餅圖顯示各項百分比到小數點第1位
'''
# --開始--批改評分使用，請勿變動
import matplotlib as mpl
mpl.use('Agg')
# --結束--批改評分使用，請勿變動

# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

# 四個月份
labels = [ 'Jun', 'Jul', 'Aug', 'Sep']
sizes = [20, 30, 40, 10]
# 圓餅圖顏色
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

# 長條圖 位置
plt.subplot(1, 2, 1)
xticks = range(1, len(labels) + 1)
# 長條圖以labels為X軸，sizes為Y軸，各長條顏色為藍色（blue）
plt.xticks(xticks, labels)
plt.bar(xticks, labels, color='blue')

# 圓餅圖 位置
plt.subplot(1, 2, 2)
# 圓餅圖以labels為圖標，sizes為各項所占百分比
# 圓餅圖colors為各項顏色，突顯「Aug」
# 圓餅圖顯示各項百分比到小數點第1位
explode = (0, 0, 0.1, 0)
plt.pie(sizes, explode=explode, labels=labels,
        colors=colors, autopct='aug')
# 長寬比為1:1
plt.axis('equal')

plt.savefig('chart.png')
plt.close()

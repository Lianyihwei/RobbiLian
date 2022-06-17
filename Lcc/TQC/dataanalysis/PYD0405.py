'''
依下列要求以matplotlib輸出chart.png圖檔：

利用程式內提供的第一組sample1與第二組sample2數據輸出左右兩個圖，
左圖為直方圖（histogram），右圖為散佈圖（scatter）。
直方圖疊合兩個直方圖，兩圖均請在-3~+3間均勻間隔分為100格，
透明度（alpha）均為0.5。在左上角放置圖例，sample1的標記為samples 1，
sample2的標記為samples 2。
散佈圖以 sample1 作為X軸資料、sample2作為Y軸資料，透明度設為 0.2。
'''
# --開始--批改評分使用，請勿變動
import matplotlib as mpl
mpl.use('Agg')
set_seed = 123
# --結束--批改評分使用，請勿變動

# 載入 numpy 模組並縮寫為 np
import numpy as np
# 載入 matplotlib.pyplot 並縮寫為 plt
import matplotlib.pyplot as plt

samples_1 = np.random.RandomState(set_seed).normal(loc=1, scale=.5, size=1000)
samples_2 = np.random.RandomState(set_seed).standard_t(df=10, size=1000)
bins = np.linspace(-3, 3, 100)

# 第一個子圖
plt.subplot(2, 2, 1)
plt.hist(samples_1, bins=bins, alpha=0.5, label='samples 1')
plt.hist(samples_2, bins=bins, alpha=0.5, label='samples 2')
# 在左上角 upper left 放置圖例 legend
plt.legend(loc='upper left')

# 第二個子圖
plt.subplot(1, 2, 2)
plt.scatter(samples_1, samples_2, alpha=0.2)

plt.savefig('chart.png')
plt.close()

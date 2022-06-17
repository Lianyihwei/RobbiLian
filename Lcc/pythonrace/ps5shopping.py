"""
輸入說明
第一列：有x個競爭者和y個購物網站
第二列：每個購物網站各有幾台ps5
接下來 
x列，代表第xi個競爭者有機率選擇的購物網站，假設他們選擇任一購物網站的機率都一樣
輸出說明
小明應該選擇第幾個購物網站，如果有多個購物網站機率相同，輸出排序靠前的那個。
"""

x,y = map(int,input().split(" "))
#建變數x,y 準備接使用者輸入有y個網路賣ps5，x個使用者準備登記
ps5 = input().split(" ")
#建數ps5，接在第幾個網站會有幾台ps5備販售

per = [0.0]*y
#建1*y的空list，預設為各網站計算推算有幾個使用者參加後購買到機率，預設為0
for i in range(x):
    buyers = input().split(" ")
    for buyer in buyers:
        per[int(buyer)-1] += (1/len(buyers))
# 共有3個使用者，buyers則是使用者預計會參加那幾個網站
# 參加網站的機率相同，所以如x1要參加2個，則參加的幾率分別是50%
# per[int(buyer)-1] <---- 使用者要參加的網站編號-1   
# += (1/len(buyers)) <---- 累加各使用者參加這個網站的幾率
ans = [0,0]
for i in range(y):
    chance = min(1, int(ps5[i]) / (per[i] + 1))
    if chance > ans[0]:
        ans = [chance,i]
# 預設1個內容為0的1*2list，[0]準備放幾率[1]放網站編號
# 再設變數chance，把機率100,跟第i個網站ps5台數/第i個網站參加購買的使用者機率加上自已的1
# 比較把min把較小的值放入chance
# 如果chaace比ans[0]的幾率大，就把[幾率,第i個網站]存入ans中

print(ans[1]+1)
# 把答案列出

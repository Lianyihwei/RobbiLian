# def coincahnge(coins,amount):
#     dp = [amount+1]*(amount+1)
#     dp[0] = 0
#     for i in range(0,amount+1):
#         for j in range(len(coins)):
#             if coins[j] <= i:
#                 dp[i] = min(dp[i],dp[i-coins[j]+1])
#     if dp[amount] > amount:
#         return -1
#     else:
#         return dp[amount]

# coins = [1,2,5]
# amount = 11
# ans = coincahnge(coins,amount)
# print(ans)
def coins_change(coins,amount):

    dp = [amount+1]*(amount+1)
    dp[0] = 0
    for i in range(1,amount+1):
        for j in range(len(coins)):
            if i>=coins[j]:
                dp[i] = min(dp[i],dp[i-coins[j]]+1)
    return -1 if dp[-1]>amount else dp[-1]

coins = [1,2,5]
amount = 11
print(coins_change(coins,amount))
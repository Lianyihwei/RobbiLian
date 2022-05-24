# TODO
n = int(input())
ans = 0

for i in range(1, n):
    ans += 1 / ((i) ** (0.5) + (i + 1) ** (0.5))
print("{:.4f}".format(ans))

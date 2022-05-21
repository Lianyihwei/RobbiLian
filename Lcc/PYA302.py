# TODO
a = int(input())
b = int(input())
ans = 0
if a % 2 != 0:
    a = a + 1
else:
    a = a
if b % 2 != 0:
    b = b - 1
else:
    b = b

for i in range(a, b + 1, 2):
    ans += i
print(ans)

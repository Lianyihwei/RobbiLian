# TODO
x = []

for i in range(10):
    num = eval(input())
    x.append(num)
x.sort()
total = x[1:-1]
print(sum(total))
print(f"{(sum(total)/8):.2f}")

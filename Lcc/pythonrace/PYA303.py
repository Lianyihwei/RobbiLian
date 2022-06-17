# TODO

a = eval(input())

for i in range(1,a+1):
    for j in range(1,i+1):
        j = i*j
        print(f"{j:4d}",end="")
    print()
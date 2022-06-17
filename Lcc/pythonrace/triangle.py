n = eval(input())
for i in range(1,n):
    for j in range(n - i):
        print(" ",end="")
    for k in range(2*i-1):
        if k == 0 or k == 2*i-1-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(2*n-1):
    print("*",end="")
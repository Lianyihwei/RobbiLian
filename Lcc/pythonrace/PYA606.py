# TODO

def compute(x, y):
    for i in range(rows):
        for j in range(cols):
            print("{:4d}".format(j-i),end="")
        print()

rows = eval(input())
cols = eval(input())
compute(rows, cols)
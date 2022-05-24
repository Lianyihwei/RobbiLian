with open("read.txt") as f :
    data = f.read()
    print(data)
num = [eval(i) for i in data.split()]

print(sum(num))
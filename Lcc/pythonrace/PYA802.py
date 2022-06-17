s = input()
sum = 0
for i in range(len(s)):
    num = ord(s[i])
    sum += num
    print("ASCII code for \'{}\' is {}".format(s[i],ord(s[i])))
print(sum)

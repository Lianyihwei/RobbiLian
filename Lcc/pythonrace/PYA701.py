nums = []
sum = 0

while True:
    num = eval(input())
    if num == -9999:
        break
    sum+=num
    nums.append(num)

print(tuple(nums))
print("Length:",len(nums)) 
print("Max:",max(nums))
print("Min:",min(nums))
print("Sum:",sum)
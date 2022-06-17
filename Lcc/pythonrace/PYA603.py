nums = []
for i in range(10):
    num= eval(input())
    nums.append(num)

nums.sort()
print(nums[-1],nums[-2],nums[-3])
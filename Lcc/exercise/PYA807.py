# TODO
from statistics import mean


nums = input()
nums = nums.split()
nums = [eval(i) for i in nums]
print("Total =",sum(nums))
print("Average =",mean(nums))

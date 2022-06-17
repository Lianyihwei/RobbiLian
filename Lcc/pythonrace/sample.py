import datetime

s = input().split()
y = int(s[0])
m = int(s[1])
d = int(s[2])
date = datetime.date(y,m ,d)
day = date.strftime("%-j")
print(day)
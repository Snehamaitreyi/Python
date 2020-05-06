#advanced way to call string
str1  ="hello"
str2 = "how are you"
print("%s,%s"%(str1,str2))

#date time
from datetime import datetime
now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
#or
date = ("%s/%s/%s"%(now.year,now.month,now.day))
time = ("%s-%s-%s"%(now.hour,now.minute,now.second))
print(date+ " " + time)
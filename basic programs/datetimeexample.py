import datetime
import time

from tzdata.zoneinfo import America

print(time.time())
print(time.asctime())


rohitha = datetime.datetime.now()
print(rohitha)
print("year:",rohitha.year)
print("month:",rohitha.month)



import calendar
s = calendar.prcal(2024)
s2=calendar.month(2004,7)
s1=calendar.isleap(2024)
print(s2)


import datetime
x= datetime.datetime.now()
from datetime import timedelta
print(x+ timedelta(days=-89))


import time
from datetime import datetime
import pytz

time1= pytz.timezone('America/New_York')
print("current Time is :",datetime.now(time1))


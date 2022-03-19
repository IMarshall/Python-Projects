import datetime

import pytz

now = datetime.datetime.now()


print(now)

print(now.tzinfo)

Portland = pytz.timezone("Asia/Kolkata")


from datetime import datetime
import pytz

year = 2012
month = 12
day = 2
hour = 13
min = 1

local_tz = pytz.timezone('Europe/Copenhagen')
local_time = local_tz.localize(datetime(year, month, day, hour, min))

utc_time = local_time.astimezone(pytz.utc)

print(f"Local time (Copenhagen): {local_time}")
print(f"UTC time: {utc_time}")

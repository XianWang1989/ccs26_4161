
import datetime
import pytz

# Given local time details
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Step 1: Create a naive datetime object (without timezone info)
local_time_naive = datetime.datetime(year, month, day, hour, minute)

# Step 2: Localize it to 'Europe/Copenhagen'
local_tz = pytz.timezone('Europe/Copenhagen')
local_time = local_tz.localize(local_time_naive)

# Step 3: Convert to UTC
utc_time = local_time.astimezone(pytz.utc)

print("Local time:", local_time)
print("UTC time:", utc_time)

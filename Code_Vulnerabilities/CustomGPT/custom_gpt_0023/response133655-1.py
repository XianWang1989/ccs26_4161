
import datetime
import pytz

# Given local time details
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object (no timezone info)
local_time_naive = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime object to Copenhagen time
local_time = local_tz.localize(local_time_naive)

# Convert to UTC
utc_time = local_time.astimezone(pytz.utc)

print("Local Time in Copenhagen:", local_time)
print("Equivalent UTC Time:", utc_time)

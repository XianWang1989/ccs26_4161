
import pytz
from datetime import datetime

# Given local time components
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object
local_time_naive = datetime(year, month, day, hour, min)

# Localize the naive datetime object to Copenhagen timezone
local_time = local_tz.localize(local_time_naive)

# Convert the localized time to UTC
utc_time = local_time.astimezone(pytz.utc)

# Output the UTC time
print("UTC Time:", utc_time)

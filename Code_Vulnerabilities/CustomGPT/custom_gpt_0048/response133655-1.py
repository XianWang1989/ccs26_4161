
import datetime
import pytz

# Define your local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Given local time components
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Create a naive datetime object (no timezone info)
local_dt = datetime.datetime(year, month, day, hour, minute)

# Localize to the local timezone
localized_dt = local_tz.localize(local_dt)

# Convert to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

print("Localized datetime:", localized_dt)
print("UTC datetime:", utc_dt)

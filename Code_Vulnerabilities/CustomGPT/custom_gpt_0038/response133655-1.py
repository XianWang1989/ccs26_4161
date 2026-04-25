
import datetime
import pytz

# Define the local time parameters
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Create a timezone object for 'Europe/Copenhagen'
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object (without timezone)
local_dt = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime to the local timezone
localized_dt = local_tz.localize(local_dt)

# Convert the localized datetime to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

print("Local time:", localized_dt)
print("UTC time:", utc_dt)

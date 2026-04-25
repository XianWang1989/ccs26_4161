
import datetime
import pytz

# Given local time
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Create a naive datetime object for local time
local_dt = datetime.datetime(year, month, day, hour, minute)

# Localize this naive datetime to the Copenhagen timezone
local_tz = pytz.timezone('Europe/Copenhagen')
localized_dt = local_tz.localize(local_dt)

# Convert the localized datetime to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Print the results
print("Local time (Copenhagen):", localized_dt)
print("UTC time:", utc_dt)

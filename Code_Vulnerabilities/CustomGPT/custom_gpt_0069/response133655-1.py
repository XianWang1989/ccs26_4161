
import datetime
import pytz

# Given local datetime components
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Create a naive datetime object
local_dt = datetime.datetime(year, month, day, hour, min)

# Localize to the Europe/Copenhagen timezone
local_tz = pytz.timezone('Europe/Copenhagen')
localized_dt = local_tz.localize(local_dt)

# Convert to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

print("Local time (Copenhagen):", localized_dt)
print("Converted UTC time:", utc_dt)

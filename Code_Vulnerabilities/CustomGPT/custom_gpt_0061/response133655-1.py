
import datetime
import pytz

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Given date and time in local time
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Create a naive datetime object (without timezone info)
local_dt = datetime.datetime(year, month, day, hour, min)

# Localize the naive datetime to the specified timezone
localized_dt = local_tz.localize(local_dt)

# Convert localized datetime to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Print the results
print("Local time (Copenhagen):", localized_dt)
print("Converted UTC time:", utc_dt)

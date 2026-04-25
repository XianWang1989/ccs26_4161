
import datetime
import pytz

# Given local time:
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Specify the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object
naive_local_dt = datetime.datetime(year, month, day, hour, min)

# Localize the naive datetime to the specified timezone
localized_dt = local_tz.localize(naive_local_dt)

# Convert the localized datetime to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Print the results
print("Local time (Copenhagen):", localized_dt)
print("UTC time:", utc_dt)


import datetime
import pytz

# Your local time information
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Create a timezone object for Europe/Copenhagen
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object (without timezone)
naive_dt = datetime.datetime(year, month, day, hour, min)

# Localize the naive datetime to Copenhagen timezone
local_dt = local_tz.localize(naive_dt)

# Convert the localized datetime to UTC
utc_dt = local_dt.astimezone(pytz.utc)

# Print the results
print("Local time (Copenhagen):", local_dt)
print("Converted UTC time:", utc_dt)


import pytz
import datetime

# Local datetime in Europe/Copenhagen
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object (without timezone)
naive_dt = datetime.datetime(year, month, day, hour, min)

# Localize the naive datetime to central European time (Copenhagen)
localized_dt = local_tz.localize(naive_dt)

# Convert localized time to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Print the results
print("Localized Time (Copenhagen):", localized_dt)
print("Converted Time (UTC):", utc_dt)

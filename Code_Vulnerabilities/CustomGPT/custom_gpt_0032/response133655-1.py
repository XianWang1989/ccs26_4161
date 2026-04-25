
import datetime
import pytz

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Given local time
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Create a naive datetime object (without timezone info)
naive_dt = datetime.datetime(year, month, day, hour, min)

# Localize the naive datetime to the local timezone
localized_dt = local_tz.localize(naive_dt)

# Convert localized datetime to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Print the results
print("Localized Time:", localized_dt)
print("UTC Time:", utc_dt)

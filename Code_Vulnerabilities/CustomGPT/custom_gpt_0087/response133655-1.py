
import pytz
import datetime

# Define the local time in Copenhagen
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Create a timezone object for 'Europe/Copenhagen'
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object
naive_dt = datetime.datetime(year, month, day, hour, min)

# Localize the naive datetime to the local timezone
localized_dt = local_tz.localize(naive_dt)

# Convert to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

print("Localized Copenhagen time:", localized_dt)
print("Converted to UTC:", utc_dt)

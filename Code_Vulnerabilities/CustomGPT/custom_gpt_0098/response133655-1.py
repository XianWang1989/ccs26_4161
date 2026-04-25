
import datetime
import pytz

# Define the local time parameters
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Specify the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object (not timezone-aware)
naive_dt = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime to the Copenhagen timezone
localized_dt = local_tz.localize(naive_dt)

# Convert the localized datetime to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

print("Localized time (Copenhagen):", localized_dt)
print("Converted time (UTC):", utc_dt)


import datetime
import pytz

# Define local time information
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Set the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object
naive_time = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime to the local timezone
localized_time = local_tz.localize(naive_time)

# Convert to UTC
utc_time = localized_time.astimezone(pytz.utc)

print("Local time (Copenhagen):", localized_time)
print("UTC time:", utc_time)

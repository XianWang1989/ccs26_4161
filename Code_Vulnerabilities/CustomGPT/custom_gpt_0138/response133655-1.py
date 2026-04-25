
import datetime
import pytz

# Define your local time details
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Specify the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object (without timezone)
naive_dt = datetime.datetime(year, month, day, hour, min)

# Localize the naive datetime to the local timezone
local_dt = local_tz.localize(naive_dt)

# Convert to UTC
utc_dt = local_dt.astimezone(pytz.utc)

# Print the result
print("Local time (Copenhagen):", local_dt)
print("Converted to UTC:", utc_dt)


import datetime
import pytz

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Local datetime components
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Create a naive datetime object
naive_dt = datetime.datetime(year, month, day, hour, min)

# Localize the naive datetime to the local timezone
local_dt = local_tz.localize(naive_dt)

# Convert to UTC
utc_dt = local_dt.astimezone(pytz.utc)

print("Local time in Copenhagen:", local_dt)
print("Corresponding UTC time:", utc_dt)

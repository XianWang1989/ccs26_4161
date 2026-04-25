
import datetime
import pytz

# Define the local time parameters
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Set the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object (without timezone info)
naive_dt = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime to the specified timezone
local_dt = local_tz.localize(naive_dt)

# Convert to UTC
utc_dt = local_dt.astimezone(pytz.utc)

# Print results
print("Local time:", local_dt)
print("UTC time:", utc_dt)

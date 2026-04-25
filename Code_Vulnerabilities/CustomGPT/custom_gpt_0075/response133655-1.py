
import datetime
import pytz

# Define the local time zone
local_tz = pytz.timezone('Europe/Copenhagen')

# Define the local time
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Create a naive datetime object
naive_dt = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime to the local time zone
local_dt = local_tz.localize(naive_dt)

# Convert to UTC
utc_dt = local_dt.astimezone(pytz.utc)

# Print the results
print("Local Time (Copenhagen):", local_dt)
print("Converted Time (UTC):", utc_dt)

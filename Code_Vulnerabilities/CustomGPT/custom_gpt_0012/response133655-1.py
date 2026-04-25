
import datetime
import pytz

# Define your local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Define the local time without timezone info
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Create a naive datetime object
local_dt = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime to the local timezone
localized_dt = local_tz.localize(local_dt)

# Convert to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Print the results
print("Local time:", localized_dt)
print("UTC time:", utc_dt)

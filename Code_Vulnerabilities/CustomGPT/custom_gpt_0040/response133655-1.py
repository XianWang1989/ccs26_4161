
import datetime
import pytz

# Given local time components
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Create a naive datetime object (without timezone info)
local_dt = datetime.datetime(year, month, day, hour, minute)

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Localize the naive datetime (convert it to local time zone)
localized_dt = local_tz.localize(local_dt)

# Convert to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Output the results
print("Local time:", localized_dt)
print("UTC time:", utc_dt)

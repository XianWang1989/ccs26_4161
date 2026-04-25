
import datetime
import pytz

# Define the local time details
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object (without timezone info)
naive_dt = datetime.datetime(year, month, day, hour, min)

# Localize the naive datetime object to the local timezone
local_dt = local_tz.localize(naive_dt)

# Convert the localized datetime to UTC
utc_dt = local_dt.astimezone(pytz.utc)

# Output the results
print("Local Time:", local_dt)
print("UTC Time:", utc_dt)


import datetime
import pytz

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Define the local time
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Create a naive datetime object (without timezone info)
local_dt = datetime.datetime(year, month, day, hour, min)

# Localize the naive datetime to the local timezone
localized_dt = local_tz.localize(local_dt)

# Convert to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Print the results
print("Localized datetime:", localized_dt)
print("Converted to UTC:", utc_dt)

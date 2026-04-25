
import datetime
import pytz

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object (without timezone info)
year = 2012
month = 12
day = 2
hour = 13
min = 1
naive_dt = datetime.datetime(year, month, day, hour, min)

# Localize the naive datetime to the Copenhagen timezone
localized_dt = local_tz.localize(naive_dt)

# Convert to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Output the results
print("Localized Time (Europe/Copenhagen):", localized_dt)
print("Converted Time (UTC):", utc_dt)

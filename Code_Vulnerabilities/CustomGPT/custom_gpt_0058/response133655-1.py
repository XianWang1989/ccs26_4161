
import datetime
import pytz

# Local time variables
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Create timezone for Copenhagen
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object
local_dt = datetime.datetime(year, month, day, hour, min)

# Localize it to Copenhagen time
localized_dt = local_tz.localize(local_dt)

# Convert to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Print results
print("Localized time (Copenhagen):", localized_dt)
print("Converted time (UTC):", utc_dt)


import datetime
import pytz

# Define your local time parameters
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime (without timezone info)
naive_dt = datetime.datetime(year, month, day, hour, min)

# Localize the naive datetime
localized_dt = local_tz.localize(naive_dt)

# Convert to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Print results
print("Local Time:", localized_dt)
print("UTC Time:", utc_dt)

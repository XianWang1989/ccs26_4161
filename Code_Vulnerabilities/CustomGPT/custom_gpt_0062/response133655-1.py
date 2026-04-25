
import datetime
import pytz

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Define your local datetime
year = 2012
month = 12
day = 2
hour = 13
minute = 1
local_dt = datetime.datetime(year, month, day, hour, minute)

# Localize the datetime to the local timezone
localized_dt = local_tz.localize(local_dt)

# Convert to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Print results
print("Local Time:", localized_dt)
print("UTC Time:", utc_dt)

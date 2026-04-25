
import datetime
import pytz

# Define the local date and time
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Create a naive datetime object
naive_dt = datetime.datetime(year, month, day, hour, minute)

# Localize to 'Europe/Copenhagen' timezone
local_tz = pytz.timezone('Europe/Copenhagen')
localized_dt = local_tz.localize(naive_dt)

# Convert to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

print("Local Time (Copenhagen):", localized_dt)
print("UTC Time:", utc_dt)

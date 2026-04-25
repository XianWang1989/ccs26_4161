
import datetime
import pytz

# Define the local time components
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Create the local timezone object
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object (without timezone)
local_dt_naive = datetime.datetime(year, month, day, hour, min)

# Localize the naive datetime object to the local timezone
local_dt_aware = local_tz.localize(local_dt_naive)

# Now convert the localized datetime to UTC
utc_dt = local_dt_aware.astimezone(pytz.utc)

# Print results
print("Localized time:", local_dt_aware)
print("Converted to UTC:", utc_dt)

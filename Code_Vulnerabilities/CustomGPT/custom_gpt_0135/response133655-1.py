
import datetime
import pytz

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Define the local datetime (naive)
year = 2012
month = 12
day = 2
hour = 13
min = 1
local_dt = datetime.datetime(year, month, day, hour, min)

# Localize to the Copenhagen timezone
localized_dt = local_tz.localize(local_dt)

# Convert to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Print the result
print("Localized time:", localized_dt)
print("UTC time:", utc_dt)

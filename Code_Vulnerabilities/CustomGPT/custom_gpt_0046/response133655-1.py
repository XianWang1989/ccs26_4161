
import datetime
import pytz

# Local time details
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Create a timezone object for Europe/Copenhagen
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object (without timezone info)
naive_dt = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime to the Copenhagen timezone
localized_dt = local_tz.localize(naive_dt)

# Convert the localized datetime to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Print the results
print("Localized Time:", localized_dt)
print("UTC Time:", utc_dt)


import datetime
import pytz

# Define local time parameters
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Specify the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object (without timezone info)
local_dt = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime to the local timezone
localized_dt = local_tz.localize(local_dt)

# Convert localized datetime to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Print the results
print("Local Time: ", localized_dt)
print("UTC Time: ", utc_dt)

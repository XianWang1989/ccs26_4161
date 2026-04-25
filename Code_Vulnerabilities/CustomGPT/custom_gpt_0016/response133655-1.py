
import datetime
import pytz

# Define the local time zone
local_tz = pytz.timezone('Europe/Copenhagen')

# Provide the local date and time
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Create a naive datetime object (no time zone info)
local_dt = datetime.datetime(year, month, day, hour, min)

# Localize the naive datetime object to the local time zone
localized_dt = local_tz.localize(local_dt)

# Convert the localized datetime to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Print the results
print("Local time:", localized_dt)
print("UTC time:", utc_dt)


import datetime
import pytz

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Local time information
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Create a naive datetime object (without timezone)
local_dt = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime to the local timezone
localized_dt = local_tz.localize(local_dt)

# Convert the localized datetime to UTC
utc_dt = localized_dt.astimezone(pytz.UTC)

# Print the results
print("Localized Time (Copenhagen):", localized_dt)
print("Converted Time (UTC):", utc_dt)

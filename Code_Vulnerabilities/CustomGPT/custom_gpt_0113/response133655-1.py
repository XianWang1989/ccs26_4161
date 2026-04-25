
import datetime
import pytz

# Given local time components
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object (not aware of any timezone)
local_dt = datetime.datetime(year, month, day, hour, min)

# Localize the datetime to the specified timezone
localized_dt = local_tz.localize(local_dt)

# Convert to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Print the results
print("Localized DateTime (Copenhagen):", localized_dt)
print("Converted DateTime (UTC):", utc_dt)

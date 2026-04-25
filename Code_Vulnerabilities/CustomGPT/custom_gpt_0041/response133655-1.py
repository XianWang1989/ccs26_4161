
import datetime
import pytz

# Given local time in Copenhagen
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Define the timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime
local_dt = datetime.datetime(year, month, day, hour, minute)

# Localize it to the local timezone
localized_dt = local_tz.localize(local_dt)

# Convert to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Print the results
print("Localized time (Copenhagen):", localized_dt)
print("Converted time (UTC):", utc_dt)

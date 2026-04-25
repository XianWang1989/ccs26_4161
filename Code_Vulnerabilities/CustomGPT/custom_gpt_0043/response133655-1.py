
import datetime
import pytz

year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object
naive_dt = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime to Copenhagen time
localized_dt = local_tz.localize(naive_dt)

# Convert the localized datetime to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

print("Localized datetime (Copenhagen):", localized_dt)
print("Converted to UTC:", utc_dt)


import datetime
import pytz

# Given local time components
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime
naive_dt = datetime.datetime(year, month, day, hour, minute)

# Localize to Copenhagen timezone
localized_dt = local_tz.localize(naive_dt)

# Convert to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Print results
print("Localized time:", localized_dt)
print("UTC time:", utc_dt)

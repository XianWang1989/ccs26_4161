
import pytz
import datetime

# Given local time components
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Define the timezone for Copenhagen
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object
naive_local_dt = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime
localized_dt = local_tz.localize(naive_local_dt)

# Convert to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Output the results
print("Localized Time:", localized_dt)
print("UTC Time:", utc_dt)

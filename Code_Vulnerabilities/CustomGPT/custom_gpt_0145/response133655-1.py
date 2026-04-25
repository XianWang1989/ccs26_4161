
import datetime
import pytz

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object for the given local time
year = 2012
month = 12
day = 2
hour = 13
min = 1
naive_dt = datetime.datetime(year, month, day, hour, min)

# Localize the naive datetime to the local timezone
localized_dt = local_tz.localize(naive_dt)

# Convert the localized datetime to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Print the results
print(f"Local Time: {localized_dt}")
print(f"UTC Time: {utc_dt}")

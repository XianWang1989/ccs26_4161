
import datetime
import pytz

# Define your local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Define the local time (year, month, day, hour, minute)
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Create a naive datetime (not timezone-aware)
naive_dt = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime into Copenhagen time
localized_dt = local_tz.localize(naive_dt)

# Convert localized datetime to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Print results
print(f"Localized (Copenhagen) Time: {localized_dt}")
print(f"Converted UTC Time: {utc_dt}")

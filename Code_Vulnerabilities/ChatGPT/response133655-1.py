
import datetime
import pytz

# Define the local time parameters
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Create a naive datetime object
naive_dt = datetime.datetime(year, month, day, hour, min)

# Localize this naive datetime object to the Europe/Copenhagen timezone
local_tz = pytz.timezone('Europe/Copenhagen')
localized_dt = local_tz.localize(naive_dt)

# Convert the localized datetime to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Print the results
print(f"Local time: {localized_dt}")
print(f"UTC time: {utc_dt}")

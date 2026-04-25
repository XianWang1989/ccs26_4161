
import datetime
import pytz

# Given local time details
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object
naive_dt = datetime.datetime(year, month, day, hour, min)

# Localize the naive datetime to the Copenhagen timezone
localized_dt = local_tz.localize(naive_dt)

# Convert the localized datetime to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

print(f'Local time in Copenhagen: {localized_dt}')
print(f'Converted UTC time: {utc_dt}')

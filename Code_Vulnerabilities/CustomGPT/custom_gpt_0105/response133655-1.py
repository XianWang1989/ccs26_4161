
import datetime
import pytz

# Define the local time details
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object
naive_dt = datetime.datetime(year, month, day, hour, min)

# Localize it to create an aware datetime object in the local timezone
local_dt = local_tz.localize(naive_dt)

# Convert to UTC
utc_dt = local_dt.astimezone(pytz.utc)

# Print the results
print(f'Local time: {local_dt} (Copenhagen time)')
print(f'UTC time: {utc_dt}')

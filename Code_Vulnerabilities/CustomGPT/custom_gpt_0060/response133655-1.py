
import datetime
import pytz

# Step 1: Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Step 2: Create a datetime object for the local time
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Assuming the given time is local time
local_time = datetime.datetime(year, month, day, hour, minute)

# Step 3: Localize the local_time to the Copenhagen timezone
localized_time = local_tz.localize(local_time)

# Step 4: Convert localized time to UTC
utc_time = localized_time.astimezone(pytz.utc)

# Output the results
print(f"Local time (Copenhagen): {localized_time}")
print(f"UTC time: {utc_time}")

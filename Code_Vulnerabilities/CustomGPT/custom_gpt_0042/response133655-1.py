
import datetime
import pytz

# Define the local time in Copenhagen
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Step 1: Create the local timezone object for Europe/Copenhagen
local_tz = pytz.timezone('Europe/Copenhagen')

# Step 2: Localize the datetime to Copenhagen time
local_time = local_tz.localize(datetime.datetime(year, month, day, hour, min))

# Step 3: Convert local time to UTC
utc_time = local_time.astimezone(pytz.utc)

# Print results
print("Local time in Copenhagen:", local_time)
print("Converted time in UTC:", utc_time)

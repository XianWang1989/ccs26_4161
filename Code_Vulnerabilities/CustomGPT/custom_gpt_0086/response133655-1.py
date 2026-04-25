
import datetime
import pytz

# Given local time details
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Step 1: Create a naive datetime object
local_time = datetime.datetime(year, month, day, hour, min)

# Step 2: Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Step 3: Localize the naive datetime to the local timezone
localized_time = local_tz.localize(local_time)

# Step 4: Convert to UTC
utc_time = localized_time.astimezone(pytz.utc)

# Print the results
print("Localized Time:", localized_time)
print("UTC Time:", utc_time)

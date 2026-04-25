
import datetime
import pytz

# Local time details
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Step 1: Create a naive datetime object
local_time = datetime.datetime(year, month, day, hour, minute)

# Step 2: Localize the naive datetime object to the specified timezone
local_tz = pytz.timezone('Europe/Copenhagen')
localized_time = local_tz.localize(local_time)

# Step 3: Convert the localized time to UTC
utc_time = localized_time.astimezone(pytz.utc)

# Display results
print("Localized Time (Copenhagen):", localized_time)
print("Converted Time (UTC):", utc_time)

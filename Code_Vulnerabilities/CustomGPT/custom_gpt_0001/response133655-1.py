
import datetime
import pytz

# Given local time values
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Step 1: Create a naive datetime object
naive_time = datetime.datetime(year, month, day, hour, minute)

# Step 2: Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Step 3: Localize the naive datetime to the local timezone
localized_time = local_tz.localize(naive_time)

# Step 4: Convert localized time to UTC
utc_time = localized_time.astimezone(pytz.UTC)

# Print the resulting UTC time
print("Local Time (Copenhagen):", localized_time)
print("Equivalent UTC Time:", utc_time)

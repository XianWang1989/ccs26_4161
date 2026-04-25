
import datetime
import pytz

# Input variables
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Step 1: Create a naive datetime object
local_naive_dt = datetime.datetime(year, month, day, hour, min)

# Step 2: Localize the naive datetime to the Europe/Copenhagen timezone
local_tz = pytz.timezone('Europe/Copenhagen')
local_dt = local_tz.localize(local_naive_dt)

# Step 3: Convert to UTC
utc_dt = local_dt.astimezone(pytz.utc)

print("Local time in Copenhagen:", local_dt)
print("Corresponding UTC time:", utc_dt)

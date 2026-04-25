
import datetime
import pytz

# Define your local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime (local time)
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Step 1: Create a naive datetime
naive_dt = datetime.datetime(year, month, day, hour, minute)

# Step 2: Localize to the local timezone
localized_dt = local_tz.localize(naive_dt)

# Step 3: Convert to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Output the results
print("Local Time:", localized_dt)
print("UTC Time:", utc_dt)

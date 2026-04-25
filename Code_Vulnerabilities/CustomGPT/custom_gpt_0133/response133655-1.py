
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

# Step 1: Create a naive datetime object (without timezone)
naive_dt = datetime.datetime(year, month, day, hour, min)

# Step 2: Localize to the local timezone
localized_dt = local_tz.localize(naive_dt)

# Step 3: Convert to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Print the results
print(f"Local Time: {localized_dt}")
print(f"UTC Time: {utc_dt}")

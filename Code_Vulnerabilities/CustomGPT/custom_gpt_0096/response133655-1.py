
import pandas as pd
import pytz
from datetime import datetime

# Define your local time parameters
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Create a tz-aware datetime object in local time
local_tz = pytz.timezone('Europe/Copenhagen')
local_time = local_tz.localize(datetime(year, month, day, hour, minute))

# Convert local time to UTC
utc_time = local_time.astimezone(pytz.utc)

print(f"Local time in Copenhagen: {local_time}")
print(f"UTC time: {utc_time}")

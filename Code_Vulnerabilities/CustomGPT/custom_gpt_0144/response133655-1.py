from datetime import datetime
import pytz

# Step 1: Create naive datetime
year = 2012; month = 12; day = 2; hour = 13; minute = 1
naive_dt = datetime(year, month, day, hour, minute)

# Step 2: Localize to Copenhagen time
copenhagen = pytz.timezone('Europe/Copenhagen')
local_dt = copenhagen.localize(naive_dt)

# Step 3: Convert to UTC
utc_dt = local_dt.astimezone(pytz.utc)

print("Local time:", local_dt)
print("UTC time:", utc_dt)

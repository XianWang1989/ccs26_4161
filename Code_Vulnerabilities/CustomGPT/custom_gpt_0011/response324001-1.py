
from datetime import datetime

# Get the current timestamp
now = datetime.now()

# Format the timestamp, rounding microseconds to 2 decimal places
timestamp = now.strftime('%d-%m-%Y %H:%M:%S.') + f"{now.microsecond // 10000:02d}"

print(timestamp)

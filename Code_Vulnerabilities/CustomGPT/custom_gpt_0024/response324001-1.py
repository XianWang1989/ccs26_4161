
from datetime import datetime

# Get the current time
now = datetime.now()

# Format the date and time, rounding microseconds to 2 decimal places
formatted_time = now.strftime('%d-%m-%Y %H:%M:%S.') + f"{now.microsecond // 10000:02d}"

print(formatted_time)


from datetime import datetime

# Get the current time
current_time = datetime.now()

# Format timestamp, rounding microseconds to 2 decimal places
formatted_time = current_time.strftime('%d-%m-%Y %H:%M:%S.') + f"{current_time.microsecond // 10000:02d}"

print(formatted_time)

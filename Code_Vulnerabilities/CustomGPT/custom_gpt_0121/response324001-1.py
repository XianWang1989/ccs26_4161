
from datetime import datetime

# Current timestamp
now = datetime.now()

# Format as string with full microseconds
timestamp_str = now.strftime('%d-%m-%Y %H:%M:%S.%f')

# Round microseconds to 2 decimal places
microseconds = int(now.microsecond / 10000)  # Convert to tens of microseconds
formatted_timestamp = timestamp_str[:-3] + f'{microseconds:02d}'

print(formatted_timestamp)

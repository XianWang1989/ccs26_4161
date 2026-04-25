
from datetime import datetime

# Get the current timestamp
now = datetime.now()

# Format the timestamp and round microseconds to 2 decimal places
formatted_timestamp = now.strftime('%d-%m-%Y %H:%M:%S.') + f'{now.microsecond // 10000:02}'  # Get tens of microseconds

print(formatted_timestamp)

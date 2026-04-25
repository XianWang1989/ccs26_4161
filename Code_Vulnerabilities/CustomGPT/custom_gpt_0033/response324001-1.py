
from datetime import datetime

# Get the current timestamp
now = datetime.now()

# Calculate tens of microseconds
tens_of_microseconds = (now.microsecond // 10000) / 100.0

# Format the timestamp
formatted_time = now.strftime(f'%d-%m-%Y %H:%M:%S.{int(tens_of_microseconds * 100)}')

print(formatted_time)

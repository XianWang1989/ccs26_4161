
from datetime import datetime

# Current timestamp
now = datetime.now()

# Get the microseconds and convert to tens of microseconds
tens_of_microseconds = now.microsecond // 10000

# Format the timestamp with rounded microseconds
formatted_time = now.strftime(f'%d-%m-%Y %H:%M:%S.{tens_of_microseconds:02d}')

print(formatted_time)

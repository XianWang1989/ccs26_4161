
from datetime import datetime

# Get the current timestamp
now = datetime.now()

# Format the timestamp with microseconds rounded to 2 decimal places
formatted_timestamp = now.strftime(f'%d-%m-%Y %H:%M:%S.{now.microsecond // 10000:02d}')

print(formatted_timestamp)

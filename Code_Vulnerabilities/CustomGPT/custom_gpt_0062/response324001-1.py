
from datetime import datetime

# Current timestamp
now = datetime.now()

# Format the timestamp, rounding microseconds to two decimal places
formatted_time = now.strftime(f'%d-%m-%Y %H:%M:%S.{now.microsecond // 10000:02d}')

print(formatted_time)

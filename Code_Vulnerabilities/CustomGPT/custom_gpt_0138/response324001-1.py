
from datetime import datetime

# Current timestamp
now = datetime.now()

# Format the timestamp with microseconds rounded to 2 decimal places
formatted_time = now.strftime(f'%d-%m-%Y %H:%M:%S.{now.microsecond // 10000:02}')
print(formatted_time)

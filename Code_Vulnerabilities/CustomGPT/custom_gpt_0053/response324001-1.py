
from datetime import datetime

# Get current timestamp
now = datetime.now()

# Format the timestamp
formatted_time = now.strftime(f'%d-%m-%Y %H:%M:%S.{now.microsecond // 10000:02d}')

print(formatted_time)

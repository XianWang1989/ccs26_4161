
from datetime import datetime

# Get current timestamp
now = datetime.now()

# Format timestamp with microseconds rounded to two decimal places
formatted_time = now.strftime('%d-%m-%Y %H:%M:%S.') + f'{now.microsecond // 10000:02d}'

print(formatted_time)

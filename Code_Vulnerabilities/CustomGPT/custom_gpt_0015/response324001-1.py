
from datetime import datetime

# Get the current timestamp
now = datetime.now()

# Format the datetime string with rounded microseconds to 2 decimal places
formatted_time = now.strftime('%d-%m-%Y %H:%M:%S.') + f'{now.microsecond // 10000:02d}'

print(formatted_time)


from datetime import datetime

# Get the current timestamp
now = datetime.now()

# Format the timestamp, rounding microseconds to 2 decimal places
# Divide microseconds by 10,000 and convert to string with 2 decimal places
formatted_time = now.strftime('%d-%m-%Y %H:%M:%S.') + f'{now.microsecond // 10000:02}'

print(formatted_time)

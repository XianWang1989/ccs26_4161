
from datetime import datetime

# Current timestamp
now = datetime.now()

# Format without unpacking all time elements
formatted_time = now.strftime('%d-%m-%Y %H:%M:%S.') + f'{now.microsecond // 10000:02}'

print(formatted_time)

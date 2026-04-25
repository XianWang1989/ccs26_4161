
from datetime import datetime

# Current timestamp
now = datetime.now()

# Format and round microseconds
formatted_time = now.strftime('%d-%m-%Y %H:%M:%S.') + f'{now.microsecond // 10000:02}'

print(formatted_time)

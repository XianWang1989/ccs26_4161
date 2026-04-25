
from datetime import datetime

# Current timestamp
now = datetime.now()

# Format to include only 2 decimals in microseconds
formatted_time = now.strftime('%d-%m-%Y %H:%M:%S.') + f'{now.microsecond // 10000:02d}'

print(formatted_time)

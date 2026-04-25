
from datetime import datetime

# Current timestamp
now = datetime.now()

# Format the timestamp
formatted_timestamp = now.strftime('%d-%m-%Y %H:%M:%S.') + f'{now.microsecond // 10000:02d}'
print(formatted_timestamp)

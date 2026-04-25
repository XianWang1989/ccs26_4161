
from datetime import datetime

# Current timestamp
now = datetime.now()

# Format the timestamp with microseconds rounded to two decimal places
formatted_timestamp = now.strftime('%d-%m-%Y %H:%M:%S.') + f"{now.microsecond // 10000:02}"

print(formatted_timestamp)

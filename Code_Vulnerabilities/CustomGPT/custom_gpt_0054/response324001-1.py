
from datetime import datetime

# Current timestamp
now = datetime.now()

# Format the timestamp with microseconds rounded to 2 decimal places (tens of microseconds)
formatted_timestamp = now.strftime('%d-%m-%Y %H:%M:%S.') + f"{round(now.microsecond / 10):02d}"

print(formatted_timestamp)

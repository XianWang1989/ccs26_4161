
from datetime import datetime

# Current timestamp
now = datetime.now()

# Format the timestamp to include microseconds rounded to 2 decimal places (tens of microseconds)
formatted_time = now.strftime('%d-%m-%Y %H:%M:%S.') + f"{now.microsecond // 10000:02d}"

print(formatted_time)

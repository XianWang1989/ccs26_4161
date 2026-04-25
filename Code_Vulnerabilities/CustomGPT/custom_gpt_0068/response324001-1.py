
from datetime import datetime

# Getting the current datetime
now = datetime.now()

# Formatting the datetime with microseconds rounded to 2 decimal places (tens of microseconds)
formatted_time = now.strftime('%d-%m-%Y %H:%M:%S.') + f"{now.microsecond // 10000:02d}"

print(formatted_time)

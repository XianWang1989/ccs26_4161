
from datetime import datetime

# Current time
now = datetime.now()

# Format timestamp with microseconds rounded to 2 decimal places
formatted_time = now.strftime('%d-%m-%Y %H:%M:%S.') + f"{now.microsecond // 10000:02d}"

print(formatted_time)

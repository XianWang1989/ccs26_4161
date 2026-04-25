
from datetime import datetime

# Sample timestamp
now = datetime.now()

# Format the timestamp to include the required rounding of microseconds
formatted_time = now.strftime('%d-%m-%Y %H:%M:%S.') + f"{now.microsecond // 10000:02d}"

print(formatted_time)

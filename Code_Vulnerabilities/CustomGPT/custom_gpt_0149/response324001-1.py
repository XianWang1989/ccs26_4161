
from datetime import datetime

# Current datetime
now = datetime.now()

# Format the timestamp, rounding microseconds to 2 decimal places
formatted_time = now.strftime('%d-%m-%Y %H:%M:%S.') + f"{now.microsecond // 10000:02d}"

# Print the result
print(formatted_time)

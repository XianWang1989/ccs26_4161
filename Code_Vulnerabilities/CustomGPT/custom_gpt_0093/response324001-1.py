
from datetime import datetime

# Get the current timestamp
now = datetime.now()

# Format the timestamp and round microseconds to two decimal places (in tens of microseconds)
formatted_time = now.strftime('%d-%m-%Y %H:%M:%S.') + f"{now.microsecond // 10000:02}"

print(formatted_time)

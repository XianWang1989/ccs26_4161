
from datetime import datetime

# Get the current timestamp
now = datetime.now()

# Format the timestamp and calculate tens of microseconds
formatted_time = now.strftime('%d-%m-%Y %H:%M:%S.') + f"{now.microsecond // 10000:02d}"

# Print the formatted timestamp
print(formatted_time)

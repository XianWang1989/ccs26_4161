
from datetime import datetime

# Get the current timestamp
now = datetime.now()

# Format the timestamp with rounded microseconds
formatted_timestamp = now.strftime('%d-%m-%Y %H:%M:%S.') + f"{now.microsecond // 10000:02d}"

print(formatted_timestamp)

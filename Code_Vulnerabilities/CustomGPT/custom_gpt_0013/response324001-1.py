
from datetime import datetime

# Get the current timestamp
now = datetime.now()

# Format the timestamp
formatted_timestamp = now.strftime('%d-%m-%Y %H:%M:%S.') + f"{int(now.microsecond / 10000)}"

print(formatted_timestamp)

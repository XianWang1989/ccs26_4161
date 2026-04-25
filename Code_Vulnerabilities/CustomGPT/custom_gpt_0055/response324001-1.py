
from datetime import datetime

# Get the current time
now = datetime.now()

# Format timestamp with microseconds rounded to 2 decimal places
formatted_timestamp = now.strftime('%d-%m-%Y %H:%M:%S.') + f"{now.microsecond / 10000:.2f}"

print(formatted_timestamp)

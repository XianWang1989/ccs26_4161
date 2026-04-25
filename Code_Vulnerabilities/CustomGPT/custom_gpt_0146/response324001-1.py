
from datetime import datetime

# Get the current datetime
now = datetime.now()

# Format the datetime and round the microseconds to 2 decimal places
formatted_time = now.strftime('%d-%m-%Y %H:%M:%S.') + f"{now.microsecond / 10000:.2f}"

print(formatted_time)

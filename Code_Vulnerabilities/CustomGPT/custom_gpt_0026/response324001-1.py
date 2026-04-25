
from datetime import datetime

# Get the current timestamp
now = datetime.now()

# Format the timestamp
formatted_time = now.strftime('%d-%m-%Y %H:%M:%S.%f')

# Round microseconds to two decimal places (in tens of microseconds)
# Slice the string to only keep two decimal points for the microseconds
formatted_time = formatted_time[:-4] + formatted_time[-3:-1]

print(formatted_time)

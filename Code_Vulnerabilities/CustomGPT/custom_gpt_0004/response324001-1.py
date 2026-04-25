
from datetime import datetime

# Current timestamp
now = datetime.now()

# Convert microseconds to tens of microseconds and format
# Rounding the microseconds to tens of microseconds (two decimal places)
formatted_time = now.strftime('%d-%m-%Y %H:%M:%S.{}').format(int(now.microsecond / 10000))

print(formatted_time)

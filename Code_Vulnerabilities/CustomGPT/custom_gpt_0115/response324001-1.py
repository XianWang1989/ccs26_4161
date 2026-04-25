
from datetime import datetime

# Current timestamp
now = datetime.now()

# Format the timestamp
formatted_time = now.strftime('%d-%m-%Y %H:%M:%S.%f')

# Convert microseconds to tens of microseconds and round to 2 decimal places
microseconds = int(now.microsecond / 10000)  # Convert to tens of microseconds
formatted_tens_microseconds = f"{microseconds / 100:.2f}"  # Format to 2 decimal places

# Combine date and time with modified microseconds
result = f"{now.strftime('%d-%m-%Y %H:%M:%S.')}{formatted_tens_microseconds.zfill(2)}"
print(result)

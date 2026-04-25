
from datetime import datetime

# Current timestamp
now = datetime.now()

# Format the timestamp
formatted_time = now.strftime('%d-%m-%Y %H:%M:%S.') + f"{now.microsecond // 10000:02d}"

# Print the formatted time
print(formatted_time)

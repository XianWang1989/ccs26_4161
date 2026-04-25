
from datetime import datetime

# Current datetime with microseconds
current_time = datetime.now()

# Format datetime with rounded microseconds to two decimal places
formatted_time = current_time.strftime('%d-%m-%Y %H:%M:%S.') + f"{current_time.microsecond // 10000:02d}"

print(formatted_time)


from datetime import datetime

# Current time
now = datetime.now()

# Format the timestamp with microseconds rounded to 2 decimal places
formatted_time = now.strftime('%d-%m-%Y %H:%M:%S.') + '{:.2f}'.format(now.microsecond / 10000)

print(formatted_time)

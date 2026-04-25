
from datetime import datetime

# Get current time
now = datetime.now()

# Format to get microseconds in tens
formatted_time = now.strftime('%d-%m-%Y %H:%M:%S.') + f"{now.microsecond // 10000:02d}"
print(formatted_time)

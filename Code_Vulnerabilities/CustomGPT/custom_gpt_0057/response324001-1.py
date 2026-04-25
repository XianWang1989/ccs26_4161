
from datetime import datetime

def format_timestamp(dt):
    rounded_microseconds = round(dt.microsecond / 10000) * 10
    dt_formatted = dt.strftime('%d-%m-%Y %H:%M:%S.')
    return f"{dt_formatted}{int(rounded_microseconds):02d}"

now = datetime.now()
formatted_timestamp = format_timestamp(now)
print(formatted_timestamp)

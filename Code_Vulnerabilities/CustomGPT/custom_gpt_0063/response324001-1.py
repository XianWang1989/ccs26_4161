
from datetime import datetime

def format_timestamp(dt):
    # Get microseconds and convert to tens of microseconds (divide by 10000)
    tens_of_microseconds = round(dt.microsecond / 10000, 2)
    # Format the timestamp
    formatted_time = dt.strftime(f'%d-%m-%Y %H:%M:%S.{int(tens_of_microseconds * 100)}')
    return formatted_time

# Example usage
now = datetime.now()
formatted_now = format_timestamp(now)
print(formatted_now)

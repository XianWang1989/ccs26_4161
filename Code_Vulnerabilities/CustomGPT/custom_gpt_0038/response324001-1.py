
from datetime import datetime

def format_timestamp(dt):
    # Get microseconds and round to tens of microseconds
    microseconds = round(dt.microsecond / 10000)  # Convert to tens of microseconds
    rounded_microseconds = f"{microseconds:02d}"  # Format to 2 decimal places

    # Format the timestamp
    formatted_time = dt.strftime(f'%d-%m-%Y %H:%M:%S.{rounded_microseconds}')
    return formatted_time

# Example usage
now = datetime.now()
formatted_now = format_timestamp(now)
print(formatted_now)

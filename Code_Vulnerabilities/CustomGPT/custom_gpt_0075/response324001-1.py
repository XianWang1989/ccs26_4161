
from datetime import datetime

def format_timestamp(dt):
    # Use strftime for base formatting
    formatted_str = dt.strftime('%d-%m-%Y %H:%M:%S.')

    # Round and format the microseconds
    microseconds = round(dt.microsecond / 10000)
    formatted_microseconds = f'{microseconds:02}'

    return formatted_str + formatted_microseconds

# Example usage
timestamp = datetime(2023, 7, 1, 12, 34, 56, 123456)
print(format_timestamp(timestamp))  # Output: 01-07-2023 12:34:56.12

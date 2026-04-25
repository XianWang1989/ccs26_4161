
from datetime import datetime, timedelta
import numpy as np

def count_day_hour_pairs(start, end, day_hour_pairs):
    current = start
    count = {}

    # Make sure to iterate over the end date
    while current <= end:
        # Get the current day of the week as a string
        day_name = current.strftime('%a')

        # Check if the current day is in the provided pairs
        if day_name in day_hour_pairs:
            for hour in day_hour_pairs[day_name]:
                # Check if the current time falls within the specific hour
                if current.hour == hour:
                    # Create a key for counting
                    key = f'{day_name}: {hour}'
                    if key not in count:
                        count[key] = 0
                    count[key] += 1

        # Move to the next hour
        current += timedelta(hours=1)

    return count

# Example parameters
start = datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime(2015, 8, 30, 10, 22, 36, 363912)

day_hour_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Call the function
result = count_day_hour_pairs(start, end, day_hour_pairs)
print(result)

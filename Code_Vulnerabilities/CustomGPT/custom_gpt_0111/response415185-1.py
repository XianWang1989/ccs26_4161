
from datetime import datetime, timedelta
import re

# Define the day-hour pairs
day_hour_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Define the start and end datetime
start = datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime(2015, 8, 30, 10, 22, 36, 363912)

def count_day_hour_pairs(start, end, day_hour_pairs):
    # Initialize a dictionary to hold counts
    counts = {day: 0 for day in day_hour_pairs.keys()}

    # Loop over each date between start and end
    current = start
    while current <= end:
        day_name = current.strftime('%a')  # Get the day of the week
        if day_name in day_hour_pairs:  # Check if it's in our pairs
            hour = current.hour  # Get the current hour
            if hour in day_hour_pairs[day_name]:  # Check for hour match
                counts[day_name] += 1
        current += timedelta(hours=1)  # Increment by one hour

    return counts

# Count the occurrences
result = count_day_hour_pairs(start, end, day_hour_pairs)
print(result)

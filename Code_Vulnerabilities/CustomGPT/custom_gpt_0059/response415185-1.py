
from datetime import datetime, timedelta
import numpy as np

# Define the day-hour pairs
day_hour_pairs = {
    'Mon': [9, 23],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Thu': [12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Define start and end datetime
start = datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime(2015, 8, 30, 10, 22, 36, 363912)

def count_day_hour(start, end, day_hour_pairs):
    # Create a dictionary to hold counts for each day-hour pair
    counts = {day: 0 for day in day_hour_pairs}

    # Generate a list of all days within the range
    current = start
    while current <= end:
        day_name = current.strftime('%a')  # Get the day name (Mon, Tue, etc.)
        if day_name in day_hour_pairs:
            hours = day_hour_pairs[day_name]
            for hour in hours:
                hour_start = current.replace(hour=hour, minute=0, second=0, microsecond=0)
                hour_end = hour_start + timedelta(hours=1)

                # Check if this hour falls within the start and end time
                if hour_end > start and hour_start < end:
                    counts[day_name] += 1
        # Move to the next day
        current += timedelta(days=1)

    return counts

# Count the occurrences for all day-hour pairs
result = count_day_hour(start, end, day_hour_pairs)
print(result)

# Example to count only "Wednesdays at 14"
def count_specific_hour(start, end, day, hour):
    count = 0
    current = start
    while current <= end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += timedelta(hours=1)
    return count

# Count for Wednesday at 14
wednesday_14_count = count_specific_hour(start, end, 'Wed', 14)
print(f"Wednesdays at 14: {wednesday_14_count}")

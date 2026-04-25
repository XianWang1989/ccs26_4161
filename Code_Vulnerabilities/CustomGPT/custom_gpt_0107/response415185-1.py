
from datetime import datetime, timedelta
import collections

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

def count_day_hour_pairs(start, end, day_hour_pairs):
    # Initialize a dictionary to store counts
    counts = collections.defaultdict(int)

    current = start
    while current <= end:
        day_name = current.strftime('%a')  # Get the day of the week
        current_hour = current.hour

        # Check if current day and hour match any pair
        if day_name in day_hour_pairs:
            if current_hour in day_hour_pairs[day_name]:
                counts[(day_name, current_hour)] += 1

        current += timedelta(hours=1)  # Move to the next hour

    return counts

# Example usage
start = datetime(2015, 7, 22, 17, 58, 54)
end = datetime(2015, 8, 30, 10, 22, 36)

result = count_day_hour_pairs(start, end, day_hour_pairs)
print(result)

# For a specific pair, e.g., "Wednesday: 14"
def count_specific_day_hour(start, end, day, hour):
    count = 0
    current = start
    while current <= end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += timedelta(hours=1)
    return count

# Example for Wednesday 14
specific_count = count_specific_day_hour(start, end, 'Wed', 14)
print(f"Count of 'Wednesday: 14' between the dates: {specific_count}")

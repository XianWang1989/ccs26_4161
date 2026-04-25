
import datetime
from collections import defaultdict

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

# Example start and end datetime
start = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

def count_day_hour_pairs(start, end, day_hour_pairs):
    current = start
    counts = defaultdict(int)

    # Create a mapping for weekdays to numbers
    week_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    # Loop through each day in the range
    while current <= end:
        if current.strftime('%a') in day_hour_pairs:
            hours = day_hour_pairs[current.strftime('%a')]
            # Count each valid hour
            if current.hour in hours:
                counts[(current.strftime('%a'), current.hour)] += 1

        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return counts

# Get the counts
result = count_day_hour_pairs(start, end, day_hour_pairs)

# Print the result
for (day, hour), count in result.items():
    print(f"{day} at {hour}:00 - Count: {count}")

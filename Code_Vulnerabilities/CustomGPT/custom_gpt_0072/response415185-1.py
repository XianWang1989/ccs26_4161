
import datetime
from collections import defaultdict

# Function to count hours for specified day-hour pairs in a datetime range
def count_day_hour_pairs(start, end, pairs):
    # Create a defaultdict to store counts
    counts = defaultdict(int)

    # Iterate through the datetime range
    current = start

    while current <= end:
        # Get the day of the week
        day_name = current.strftime('%a')  # Abbreviated day name (e.g., 'Wed')

        # If the day is in our pairs
        if day_name in pairs:
            # Check each hour for that day
            for hour in pairs[day_name]:
                # If the hour fits within the current time
                if hour == current.hour:
                    counts[(day_name, hour)] += 1

        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return counts

# Day-hour pairs
day_hour_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Datetime range
start_dt = datetime.datetime(2015, 7, 22, 17, 58, 54)
end_dt = datetime.datetime(2015, 8, 30, 10, 22, 36)

# Count the occurrences
result = count_day_hour_pairs(start_dt, end_dt, day_hour_pairs)

# Print the results
for (day, hour), count in result.items():
    print(f'{day} {hour}: {count}')

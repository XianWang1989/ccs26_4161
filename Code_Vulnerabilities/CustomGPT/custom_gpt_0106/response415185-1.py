
import datetime
from collections import defaultdict

def count_day_hour_pairs(start, end, day_hour_pairs):
    # Create a default dictionary to hold counts
    counts = defaultdict(int)

    # Generate the full range of dates
    current = start
    while current <= end:
        day_name = current.strftime('%a')  # Get the day name (Mon, Tue, etc.)
        hour = current.hour

        # Check if the current day and hour match any pairs
        if day_name in day_hour_pairs and hour in day_hour_pairs[day_name]:
            counts[(day_name, hour)] += 1

        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return counts

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
start_datetime = datetime.datetime(2015, 7, 22, 17, 58, 54)
end_datetime = datetime.datetime(2015, 8, 30, 10, 22, 36)

# Count the day-hour pairs
result = count_day_hour_pairs(start_datetime, end_datetime, day_hour_pairs)

# Print the results
for key, count in result.items():
    print(f"{key}: {count}")

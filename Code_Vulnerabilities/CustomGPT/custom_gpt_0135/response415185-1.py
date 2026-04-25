
import datetime
from collections import defaultdict

# Define the day-of-week-hour pairs
day_hour_mapping = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Define the start and end datetime
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

def count_day_hour_pairs(start, end, day_hour_mapping):
    counts = defaultdict(int)

    # Create a current datetime variable starting from 'start'
    current = start

    while current <= end:
        # Get the day name and hour
        day_name = current.strftime("%a")  # Short week day (e.g., Mon, Tue)
        hour = current.hour

        # Check if this day has relevant hours
        if day_name in day_hour_mapping and hour in day_hour_mapping[day_name]:
            counts[(day_name, hour)] += 1

        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return counts

# Execute the function
result = count_day_hour_pairs(start, end, day_hour_mapping)

# Print the results
for day_hour, count in result.items():
    print(f"{day_hour}: {count}")

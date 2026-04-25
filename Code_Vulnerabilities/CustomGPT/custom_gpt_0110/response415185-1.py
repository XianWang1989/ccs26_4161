
import datetime
from collections import defaultdict

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
    # Create a dictionary to hold counts for each day-hour pair
    counts = defaultdict(int)

    # Iterate through each day in the range
    current_day = start
    while current_day <= end:
        day_name = current_day.strftime('%a')  # Get the day of the week
        if day_name in day_hour_pairs:
            for hour in day_hour_pairs[day_name]:
                # Count hours only if they fall into the range
                if current_day.hour == hour:
                    counts[(day_name, hour)] += 1
        # Move to the next hour
        current_day += datetime.timedelta(hours=1)

    return counts

# Define the start and end datetimes
start = datetime.datetime(2015, 7, 22, 17, 58)
end = datetime.datetime(2015, 8, 30, 10, 22)

# Count the occurrences
results = count_day_hour_pairs(start, end, day_hour_pairs)

# Print the results
for key, value in results.items():
    print(f"{key}: {value}")


import datetime
from collections import defaultdict

# Define the day-hour pairs
schedule = {
    'Mon': [9, 23],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Thu': [12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': []
}

# Function to count hours for the given day-hour pairs
def count_day_hour_pairs(start, end, schedule):
    total_counts = defaultdict(int)

    # Ensure end is greater than start
    if start > end:
        return total_counts

    current = start

    while current <= end:
        day_name = current.strftime('%a')  # Get the day's name (e.g., 'Mon')
        hour = current.hour

        if day_name in schedule and hour in schedule[day_name]:
            total_counts[(day_name, hour)] += 1

        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return total_counts

# Example datetime objects
start = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

# Calculate the counts
counts = count_day_hour_pairs(start, end, schedule)

# Display the results
for (day, hour), count in counts.items():
    print(f"{day} at {hour}:00 - Count: {count}")

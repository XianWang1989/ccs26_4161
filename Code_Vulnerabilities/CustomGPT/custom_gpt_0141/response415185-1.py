
from datetime import datetime, timedelta
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
    # Create a default dictionary to hold counts
    counts = defaultdict(int)

    # Initialize the current date to the start date
    current_date = start

    # Iterate through each day in the date range
    while current_date <= end:
        # Get the day of the week (e.g., 'Mon', 'Tue', ...)
        day_name = current_date.strftime('%a')  # Abbreviated day name

        # Get the hours for the current day
        current_hours = day_hour_pairs.get(day_name, [])

        # Count the occurrence of each hour for that day
        if current_hours:
            hour = current_date.hour
            if hour in current_hours:
                counts[(day_name, hour)] += 1

        # Move to the next day
        current_date += timedelta(days=1)

    return dict(counts)

# Example usage
start = datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime(2015, 8, 30, 10, 22, 36, 363912)

results = count_day_hour_pairs(start, end, day_hour_pairs)

# Output the results
for (day, hour), count in results.items():
    print(f"{day} at hour {hour}: {count} occurrences")

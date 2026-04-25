
from datetime import datetime, timedelta
from collections import defaultdict

# Define the day-of-week-hour pairs
day_hour_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Define start and end datetime points
start = datetime(2015, 7, 22, 17, 58, 54)
end = datetime(2015, 8, 30, 10, 22, 36)

# Function to count day-of-week-hour pairs between two dates
def count_day_hour_pairs(start, end, day_hour_pairs):
    count = defaultdict(int)

    current = start
    while current <= end:
        day_name = current.strftime('%a')  # Get the day of the week (Mon, Tue, etc.)
        if day_name in day_hour_pairs:
            for hour in day_hour_pairs[day_name]:
                # Count occurrences of the specified hour
                if current.hour <= hour < (current.hour + 1) or \
                   (current.hour == hour and current.minute == 0):  # Count only if at the beginning of the hour
                    count[(day_name, hour)] += 1

        # Move to the next hour
        current += timedelta(hours=1)
        # Reset minutes and seconds
        current = current.replace(minute=0, second=0, microsecond=0)

    return count

# Execute the function
result = count_day_hour_pairs(start, end, day_hour_pairs)

# Print the result
for key, val in result.items():
    print(f"{key}: {val}")

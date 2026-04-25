
from datetime import datetime, timedelta
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

# Function to count pairs between two datetimes
def count_day_hour_pairs(start, end, pairs):
    # Create a dictionary to hold the count of hours
    counts = defaultdict(int)

    # Initialize current datetime to the start datetime
    current = start

    # Loop through each day until the end date
    while current <= end:
        day_name = current.strftime('%a')  # Get day name (Mon, Tue, etc.)
        current_hour = current.hour         # Current hour

        # Check if the current day is in the pairs and if the hour is in the corresponding list
        if day_name in pairs and current_hour in pairs[day_name]:
            counts[(day_name, current_hour)] += 1

        # Move to the next hour
        if current.hour == 23:
            current = current + timedelta(days=1)  # Move to next day at midnight
            current = current.replace(hour=0, minute=0, second=0, microsecond=0)
        else:
            current += timedelta(hours=1)  # Next hour

    return dict(counts)

# Example usage
start_time = datetime(2015, 7, 22, 17, 58, 54)
end_time = datetime(2015, 8, 30, 10, 22, 36)
result = count_day_hour_pairs(start_time, end_time, day_hour_pairs)

# Output the result
print(result)

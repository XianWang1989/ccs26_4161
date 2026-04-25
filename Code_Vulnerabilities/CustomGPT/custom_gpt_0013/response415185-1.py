
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

# Function to count the hours for a specific day-hour pair
def count_day_hour(start: datetime.datetime, end: datetime.datetime, day: str, hours: list) -> int:
    count = 0
    current = start

    # Iterate through each week
    while current < end:
        if current.strftime('%a') == day:
            # Count the specified hours
            for hour in hours:
                # Create datetime objects for the specified hour
                hour_dt = current.replace(hour=hour, minute=0, second=0, microsecond=0)
                if start <= hour_dt < end:
                    count += 1
        current += datetime.timedelta(days=1)

    return count

# Example usage
start_datetime = datetime.datetime(2015, 7, 22, 17, 58, 54)
end_datetime = datetime.datetime(2015, 8, 30, 10, 22, 36)

# Calculate occurrences for each day-hour pair
result = defaultdict(int)
for day, hours in day_hour_pairs.items():
    result[day] = count_day_hour(start_datetime, end_datetime, day, hours)

# Print the results
for day, count in result.items():
    print(f'{day}: {count}')

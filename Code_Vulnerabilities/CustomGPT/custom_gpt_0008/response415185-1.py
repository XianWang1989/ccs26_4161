
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

def count_day_hour_pairs(start, end, day_hour_pairs):
    current = start
    count = defaultdict(int)

    # Adjust the current datetime to the next hour
    current = current.replace(minute=0, second=0, microsecond=0)

    while current <= end:
        # Get the day of the week (0=Mon, 1=Tue, ..., 6=Sun)
        day_name = current.strftime('%a')  # E.g., 'Mon', 'Tue'

        # If the day name is in the defined pairs
        if day_name in day_hour_pairs:
            # Check if the current hour is in the day's hours
            if current.hour in day_hour_pairs[day_name]:
                count[(day_name, current.hour)] += 1

        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return dict(count)

# Example usage
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)
result = count_day_hour_pairs(start, end, day_hour_pairs)

print(result)

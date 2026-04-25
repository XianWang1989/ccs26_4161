
import datetime
from collections import defaultdict

# Define your day-of-week-hour pairs
day_hour_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Your start and end datetime
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

def count_day_hour(start, end, day_hour_pairs):
    # Create a count dictionary
    count = defaultdict(int)

    # Get the start and end week day
    current = start
    while current <= end:
        # Get the current day of the week (0=Monday, 6=Sunday)
        current_day = current.strftime("%a")

        # Check if the current day is in our pairs
        if current_day in day_hour_pairs:
            # Check hours for that day
            for hour in day_hour_pairs[current_day]:
                # Create datetime for the current hour
                hour_time = current.replace(hour=hour, minute=0, second=0, microsecond=0)

                # Check if it's in the range
                if start <= hour_time <= end:
                    count[(current_day, hour)] += 1

        # Move to the next day
        current += datetime.timedelta(days=1)

    return count

# Example usage:
result = count_day_hour(start, end, day_hour_pairs)
print(result)

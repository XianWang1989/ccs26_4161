
import datetime
from collections import defaultdict

def count_day_hour_between(start, end, day_hour_pairs):
    # Create a mapping for days to indices
    day_mapping = {
        'Mon': 0,
        'Tue': 1,
        'Wed': 2,
        'Thu': 3,
        'Fri': 4,
        'Sat': 5,
        'Sun': 6
    }

    # Create a results dictionary to hold counts
    counts = defaultdict(int)

    # Iterate through the date range
    current = start
    while current <= end:
        day_name = current.strftime('%a')
        hour = current.hour

        # Check if it's a day we care about and if the hour is included
        if day_name in day_hour_pairs:
            if hour in day_hour_pairs[day_name]:
                counts[(day_name, hour)] += 1

        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return counts

# Example usage
start_time = datetime.datetime(2015, 7, 22, 17, 58, 54)  # starting from Wednesday
end_time = datetime.datetime(2015, 8, 30, 10, 22, 36)

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

# Count hours
result = count_day_hour_between(start_time, end_time, day_hour_pairs)
print(result)

# To specifically count "Wednesdays at 14"
wednesday_14_count = result.get(('Wed', 14), 0)
print(f"Wednesdays at 14: {wednesday_14_count}")

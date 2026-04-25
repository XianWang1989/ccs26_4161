
import datetime
from collections import defaultdict

def count_day_hour_pairs(start, end, day_hour_map):
    # Convert end datetime to a datetime object (if not already)
    if end < start:
        raise ValueError("End datetime must be greater than start datetime.")

    # Prepare a dictionary to count occurrences
    count = defaultdict(int)

    # Create a mapping of days to their numerical value
    day_map = {
        'Mon': 0,
        'Tue': 1,
        'Wed': 2,
        'Thu': 3,
        'Fri': 4,
        'Sat': 5,
        'Sun': 6,
    }

    # Iterate over each day in the range
    current = start
    while current <= end:
        # Get the day of the week
        day_name = current.strftime('%a')  # e.g., 'Wed'

        # Check if this day is in our map
        if day_name in day_hour_map:
            # Get the matching hours for the current day
            hours = day_hour_map[day_name]

            # Check if the current hour is one of the specified hours
            if current.hour in hours:
                count[(day_name, current.hour)] += 1

        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return dict(count)

# Example inputs
start = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

day_hour_map = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Count occurrences
result = count_day_hour_pairs(start, end, day_hour_map)
print(result)

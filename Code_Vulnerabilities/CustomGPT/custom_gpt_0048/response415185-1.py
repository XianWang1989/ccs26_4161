
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

# Define the start and end datetime
start = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

def count_day_hour_pairs(start, end, day_hour_dict):
    # Initialize a dictionary to hold counts
    counts = defaultdict(int)

    # Create a date range
    current_date = start
    while current_date <= end:
        # Check the day of the week
        day_name = current_date.strftime('%a')

        # Check if the current hour is in the specified hours for that day
        if day_name in day_hour_dict:
            if current_date.hour in day_hour_dict[day_name]:
                counts[day_name] += 1

        # Move to the next hour
        current_date += datetime.timedelta(hours=1)

    return dict(counts)

# Get the counts
result = count_day_hour_pairs(start, end, day_hour_pairs)

# Print the result
print(result)

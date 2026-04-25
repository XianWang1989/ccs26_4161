
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
    'Sun': []
}

def count_day_hour_pairs(start, end, pairs):
    # Initialize a dictionary to hold counts
    count_matrix = defaultdict(int)

    # Prepare to iterate through the date range
    current_date = start
    while current_date <= end:
        day_name = current_date.strftime('%a')  # Get the day of the week
        hour = current_date.hour  # Get the current hour

        # Check if the current hour is in the specified pairs
        if day_name in pairs:
            if hour in pairs[day_name]:
                count_matrix[(day_name, hour)] += 1

        # Move to the next hour
        current_date += timedelta(hours=1)

    return dict(count_matrix)

# Sample datetime objects
start_datetime = datetime(2015, 7, 22, 17, 58, 54)
end_datetime = datetime(2015, 8, 30, 10, 22, 36)

# Count occurrences
result = count_day_hour_pairs(start_datetime, end_datetime, day_hour_pairs)
print(result)

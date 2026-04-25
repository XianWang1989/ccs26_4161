
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

def count_day_hour_pairs(start, end, pairs):
    # Create a count dictionary to hold the results
    count = defaultdict(int)

    # Get the total number of days in the range
    current = start
    while current <= end:
        day_name = current.strftime('%a')  # Get the day name (e.g., Mon, Tue, etc.)
        hour = current.hour  # Get the current hour

        # If the day is in our pairs, check the hours
        if day_name in pairs:
            if hour in pairs[day_name]:
                # Increment the count for this pair
                count[(day_name, hour)] += 1

        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return dict(count)

# Example usage
start_datetime = datetime.datetime(2015, 7, 22, 17, 58, 54)
end_datetime = datetime.datetime(2015, 8, 30, 10, 22, 36)

result = count_day_hour_pairs(start_datetime, end_datetime, day_hour_pairs)

# Print the results
for key, value in result.items():
    print(f"{key}: {value}")

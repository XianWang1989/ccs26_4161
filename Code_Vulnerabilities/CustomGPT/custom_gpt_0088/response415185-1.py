
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

# Function to count occurrences of day-hour pairs between two datetime points
def count_day_hour_pairs(start, end, day_hour_pairs):
    count = defaultdict(int)
    current = start

    # Iterate through each hour from start to end
    while current <= end:
        day_name = current.strftime('%a')  # Get the day name
        hour = current.hour

        # Check if the current hour is in the specified day-hours
        if hour in day_hour_pairs.get(day_name, []):
            count[(day_name, hour)] += 1

        # Increment the current time by one hour
        current += datetime.timedelta(hours=1)

    return dict(count)

# Set the start and end datetime objects
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

# Get the counts
result = count_day_hour_pairs(start, end, day_hour_pairs)

# Print the result
for (day, hour), cnt in result.items():
    print(f"{day} {hour}: {cnt} occurrences")

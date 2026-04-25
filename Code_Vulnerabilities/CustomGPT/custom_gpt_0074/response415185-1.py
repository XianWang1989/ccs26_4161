
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

def count_day_hour_pairs(start, end, day_hour_dict):
    current = start
    counts = defaultdict(int)  # To store counts of each day-hour pair

    # Loop until we reach the end date
    while current <= end:
        day_name = current.strftime("%a")  # Get the day of the week name (Mon, Tue, etc.)
        hour = current.hour  # Get the current hour

        if day_name in day_hour_dict and hour in day_hour_dict[day_name]:
            counts[(day_name, hour)] += 1

        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return counts

# Define your start and end datetime
start = datetime.datetime(2015, 7, 22, 17, 58)
end = datetime.datetime(2015, 8, 30, 10, 22)

# Get the counts
counts = count_day_hour_pairs(start, end, day_hour_pairs)

# Print the result
for (day, hour), count in counts.items():
    print(f'{day} at {hour}:00 => {count} occurrences')

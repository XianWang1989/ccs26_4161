
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
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

# Initialize a counter for each day-hour pair
counts = defaultdict(int)

# Loop through each day in the range
current = start
while current <= end:
    day_name = current.strftime('%a')  # Get the day name (Mon, Tue, ...)
    hour = current.hour  # Get the hour in 24H format

    # Check if the day and hour are in the dictionary
    if day_name in day_hour_pairs and hour in day_hour_pairs[day_name]:
        counts[(day_name, hour)] += 1

    # Move to the next hour
    current += datetime.timedelta(hours=1)

# Display the counted pairs
for (day, hour), count in counts.items():
    print(f"{day}: {hour} => {count} occurrences")

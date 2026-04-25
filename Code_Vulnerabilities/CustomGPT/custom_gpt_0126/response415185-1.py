
from datetime import datetime, timedelta
from collections import defaultdict

# Define the day-of-week-hour pairs
schedule = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Define the start and end datetime
start = datetime(2015, 7, 22, 17, 58, 54)
end = datetime(2015, 8, 30, 10, 22, 36)

# Initialize a dictionary to count occurrences
count_dict = defaultdict(int)

# Iterate over each day in the date range
current = start
while current <= end:
    day_name = current.strftime('%a')  # Get the day name (e.g., 'Mon', 'Tue')
    if day_name in schedule:
        for hour in schedule[day_name]:
            # Check if the current time falls within the specified hour
            if current.hour == hour:
                count_dict[(day_name, hour)] += 1

    # Move to the next day
    current += timedelta(days=1)

# Display the counts
for key, value in count_dict.items():
    print(f"{key[0]}: {key[1]} -> {value} occurrences")

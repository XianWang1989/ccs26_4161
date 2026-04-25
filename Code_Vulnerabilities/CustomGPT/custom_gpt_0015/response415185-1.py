
import datetime
from collections import defaultdict

# Day-of-week-hour pairs
day_hour_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Date range
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

# Function to count occurrences of day-hour pairs
def count_day_hour_occurrences(day_hour_dict, start, end):
    # Create a defaultdict to keep the count
    counts = defaultdict(int)

    current = start

    # Loop through each week between start and end dates
    while current <= end:
        # Get the day of the week as a string ('Mon', 'Tue', ...)
        day_name = current.strftime("%a")  # abbreviated day name

        # If the day is in our dictionary
        if day_name in day_hour_dict:
            for hour in day_hour_dict[day_name]:
                if current.hour == hour:
                    counts[(day_name, hour)] += 1

        # Move to the next day
        current += datetime.timedelta(days=1)

    return counts

# Count occurrences
occurrences = count_day_hour_occurrences(day_hour_pairs, start, end)

# Print results
for key, count in occurrences.items():
    print(f"{key}: {count}")

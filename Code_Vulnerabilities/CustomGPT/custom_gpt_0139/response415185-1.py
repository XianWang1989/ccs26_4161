
from datetime import datetime, timedelta
from collections import defaultdict

# Define your day-hour mapping
time_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

def count_day_hour_pairs(start, end, time_pairs):
    count = defaultdict(int)

    # Start from the start date and iterate day by day until the end date
    current = start
    while current <= end:
        day_name = current.strftime("%a")  # Get the day name (e.g., 'Mon', 'Tue', etc.)
        hour = current.hour

        # If the day is in our time pairs, check if the hour is one of the specified hours
        if day_name in time_pairs and hour in time_pairs[day_name]:
            count[(day_name, hour)] += 1

        # Move to the next hour
        current += timedelta(hours=1)

    return dict(count)

# Define start and end dates
start = datetime(2015, 7, 22, 17, 58, 54)
end = datetime(2015, 8, 30, 10, 22, 36)

# Count occurrences for the provided day-hour pairs
pair_counts = count_day_hour_pairs(start, end, time_pairs)
print(pair_counts)

# Example for a specific "Wednesdays: 14"
def count_specific_day_hour(start, end, day, hour):
    count = 0
    current = start
    while current <= end:
        if current.strftime("%a") == day and current.hour == hour:
            count += 1
        current += timedelta(hours=1)
    return count

# Count occurrences of 'Wed: 14'
wednesday_14_count = count_specific_day_hour(start, end, 'Wed', 14)
print("Count of Wednesdays at 14:00:", wednesday_14_count)

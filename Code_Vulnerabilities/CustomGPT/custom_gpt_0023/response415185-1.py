
from datetime import datetime, timedelta
from collections import defaultdict

# Day-hour mapping
day_hour_mapping = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

def count_day_hour_pairs(start, end, mapping):
    # Create a counter for results
    results = defaultdict(int)

    # Move to the start of the first hour
    current = start.replace(minute=0, second=0, microsecond=0)

    # Loop through each hour until we reach the end
    while current <= end:
        day_name = current.strftime('%a')  # Get the day of the week (Mon, Tue, ...)
        hour = current.hour

        if day_name in mapping and hour in mapping[day_name]:
            results[(day_name, hour)] += 1

        # Move to the next hour
        current += timedelta(hours=1)

    return dict(results)

# Define start and end datetime
start_dt = datetime(2015, 7, 22, 17, 58, 54)
end_dt = datetime(2015, 8, 30, 10, 22, 36)

# Count the hour occurrences
result = count_day_hour_pairs(start_dt, end_dt, day_hour_mapping)

# Print the results
for key, count in result.items():
    print(f"{key}: {count}")

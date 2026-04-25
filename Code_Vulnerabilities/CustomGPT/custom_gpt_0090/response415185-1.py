
from datetime import datetime, timedelta
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

# Function to count occurrences
def count_day_hour_pairs(start, end, day_hour_dict):
    current = start
    counts = defaultdict(int)

    while current <= end:
        day_name = current.strftime('%a')  # Get the day of the week
        if day_name in day_hour_dict:
            hour = current.hour
            if hour in day_hour_dict[day_name]:  # Check if hour matches
                counts[(day_name, hour)] += 1
        current += timedelta(hours=1)  # Increment by one hour

    return counts

# Define start and end datetime
start_dt = datetime(2015, 7, 22, 17, 58, 54)
end_dt = datetime(2015, 8, 30, 10, 22, 36)

# Get counts
result = count_day_hour_pairs(start_dt, end_dt, day_hour_pairs)

# Display results
print(result)

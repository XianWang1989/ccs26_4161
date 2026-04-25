
from datetime import datetime, timedelta

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

def count_day_hour_pairs(start, end, day_hour_pairs):
    # Initialize a dictionary to hold counts
    counts = {day: 0 for day in day_hour_pairs}

    current = start
    while current <= end:
        day_name = current.strftime("%a")  # Get day of the week (e.g., 'Mon', 'Tue')
        current_hour = current.hour  # Get current hour in 24H format

        if day_name in day_hour_pairs and current_hour in day_hour_pairs[day_name]:
            counts[day_name] += 1

        # Move to the next hour
        current += timedelta(hours=1)

    return counts

# Define the start and end datetime
start = datetime(2015, 7, 22, 17, 58, 54)
end = datetime(2015, 8, 30, 10, 22, 36)

# Count day-hour pairs
result = count_day_hour_pairs(start, end, day_hour_pairs)

# Display the results
print(result)

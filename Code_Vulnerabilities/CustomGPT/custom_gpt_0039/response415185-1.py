
from datetime import datetime, timedelta

# Given datetime range
start = datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime(2015, 8, 30, 10, 22, 36, 363912)

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

# Function to count occurrences for each day-hour pair
def count_day_hour_pairs(start, end, day_hour_pairs):
    count_dict = {day: 0 for day in day_hour_pairs.keys()}

    # Loop through each day in the range
    current = start
    while current <= end:
        if current.strftime('%a') in day_hour_pairs:  # Check if it's in the specified days
            if current.hour in day_hour_pairs[current.strftime('%a')]:  # Check if the hour matches
                count_dict[current.strftime('%a')] += 1
        current += timedelta(hours=1)  # Move to the next hour

    return count_dict

# Count occurrences
occurrences = count_day_hour_pairs(start, end, day_hour_pairs)

# Print results
for day, count in occurrences.items():
    print(f"{day}: {count} occurrences")

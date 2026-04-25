
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

# Function to count occurrences of a specific day-hour pair
def count_specific_day_hour(start, end, day, hour):
    occurrence_count = 0
    current = start

    # Loop through each week from start to end
    while current <= end:
        # Check if the day matches
        if current.strftime('%a') == day and current.hour == hour:
            occurrence_count += 1
        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return occurrence_count

# Count occurrences for a specific pair: Wednesday at 14:00
wednesday_14_count = count_specific_day_hour(start, end, 'Wed', 14)
print(f'Occurrences of Wednesdays at 14:00: {wednesday_14_count}')

# Function to count occurrences for all day-hour pairs
def count_all_day_hour_pairs(start, end, pairs):
    result = defaultdict(int)

    current = start
    while current <= end:
        day = current.strftime('%a')
        if day in pairs:
            for hour in pairs[day]:
                if current.hour == hour:
                    result[(day, hour)] += 1
        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return result

# Count occurrences for all specified pairs
all_counts = count_all_day_hour_pairs(start, end, day_hour_pairs)

# Display results
for (day, hour), count in all_counts.items():
    print(f'Occurrences of {day} at {hour}:00 -> {count}')

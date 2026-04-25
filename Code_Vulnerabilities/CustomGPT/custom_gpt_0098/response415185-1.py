
import datetime

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
start_time = datetime.datetime(2015, 7, 22, 17, 58, 54)
end_time = datetime.datetime(2015, 8, 30, 10, 22, 36)

# Function to count the occurrences of day-hour pairs
def count_day_hour_occurrences(start, end, pairs):
    # Initialize a dictionary to hold counts
    counts = {day: 0 for day in pairs}

    # Generate a list of all days in the range
    current_day = start
    while current_day <= end:
        if current_day.strftime('%a') in pairs:  # Check if the current day is in pairs
            current_hour = current_day.hour
            if current_hour in pairs[current_day.strftime('%a')]:  # Check hour
                counts[current_day.strftime('%a')] += 1
        current_day += datetime.timedelta(hours=1)

    return counts

# Count occurrences
occurrences = count_day_hour_occurrences(start_time, end_time, day_hour_pairs)

# Print the results
print("Occurrences of day-hour pairs:")
for day, count in occurrences.items():
    print(f"{day}: {count}")

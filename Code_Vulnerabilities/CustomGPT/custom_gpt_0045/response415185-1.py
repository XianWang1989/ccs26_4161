
from datetime import datetime, timedelta

# Define the day-of-week-hour pairs
dow_hours = {
    'Mon': [9, 23],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Thu': [12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Define the start and end datetime points
start = datetime(2015, 7, 22, 17, 58, 54)
end = datetime(2015, 8, 30, 10, 22, 36)

# Function to count occurrences of day-hour pairs
def count_dow_hour_pairs(start, end, dow_hours):
    current_time = start
    # Initialize counts
    counts = {key: 0 for key in dow_hours.keys()}

    # Iterate through each hour between start and end
    while current_time <= end:
        weekday = current_time.strftime('%a')  # Get the weekday abbreviation (e.g., 'Wed')
        hour = current_time.hour  # Get the hour (0-23)

        # Check if the current day and hour are in the defined pairs
        if weekday in dow_hours and hour in dow_hours[weekday]:
            counts[weekday] += 1

        current_time += timedelta(hours=1)  # Move to the next hour

    return counts

# Get the counts
counts = count_dow_hour_pairs(start, end, dow_hours)

# Display the results
for day, count in counts.items():
    print(f"{day}: {count}")

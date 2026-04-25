
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

# Define the start and end datetime
start = datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime(2015, 8, 30, 10, 22, 36, 363912)

# Function to count occurrences of day-hour pairs
def count_day_hour_pairs(start, end, day_hour_pairs):
    count = {key: 0 for key in day_hour_pairs.keys()}

    # Iterate through each day in the range
    current = start
    while current <= end:
        day_name = current.strftime("%a")  # Get the day name (e.g., Mon, Tue)
        if day_name in day_hour_pairs:
            hour = current.hour
            # Check if the current hour is in the predefined hour list for that day
            if hour in day_hour_pairs[day_name]:
                count[day_name] += 1
        current += timedelta(hours=1)  # Move to the next hour

    return count

# Count the occurrences
result = count_day_hour_pairs(start, end, day_hour_pairs)

# Display the result
print(result)

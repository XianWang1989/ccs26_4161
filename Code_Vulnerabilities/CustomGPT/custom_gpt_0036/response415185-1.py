
import datetime

def count_day_hour_pairs(start, end, day_hour_pairs):
    current = start
    total_count = {day: 0 for day in day_hour_pairs.keys()}

    # Iterate through each day from start to end
    while current <= end:
        day_name = current.strftime("%a")  # Get the day of the week as 'Mon', 'Tue', etc.
        hour = current.hour  # Get the current hour

        # Check if the day is in our pairs
        if day_name in day_hour_pairs:
            # Check if the hour is within the allowed hours
            if hour in day_hour_pairs[day_name]:
                total_count[day_name] += 1

        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return total_count

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
start = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

# Count the day-hour pairs
result = count_day_hour_pairs(start, end, day_hour_pairs)

print(result)

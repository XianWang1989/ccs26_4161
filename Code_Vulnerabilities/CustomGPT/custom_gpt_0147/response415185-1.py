
import datetime

# Define the day-of-week-hour pairs
day_hour_pairs = {
    'Mon': [9, 23],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Thu': [12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

def count_hour_pairs(start, end, day_hour_dict):
    total_counts = {}

    # Create a datetime range between start and end
    current = start
    delta = datetime.timedelta(hours=1)

    # Iterate over each hour in the range
    while current <= end:
        dow = current.strftime("%a")  # Get day of the week as 'Mon', 'Tue', etc.
        hour = current.hour  # Get current hour

        # Check if the current day is in the dictionary and hour is in the list
        if dow in day_hour_dict and hour in day_hour_dict[dow]:
            if (dow, hour) not in total_counts:
                total_counts[(dow, hour)] = 0
            total_counts[(dow, hour)] += 1

        current += delta  # Move to the next hour

    return total_counts

# Define the start and end datetime
start_dt = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end_dt = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

# Get the counts for day-hour pairs
results = count_hour_pairs(start_dt, end_dt, day_hour_pairs)

# Print results
for key, count in results.items():
    print(f"{key[0]}: {key[1]} -> {count} occurrences")

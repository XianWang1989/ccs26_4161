
import datetime

# Define the day-hour pairs
day_hour_pairs = {
    'Mon': [9, 23],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Thu': [12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': []
}

def count_day_hour_pairs(start, end, day_hour_pairs):
    # Initialize a dictionary to store counts
    counts = {day: 0 for day in day_hour_pairs.keys()}

    # Iterate through each day in the range
    current_date = start
    while current_date <= end:
        current_day = current_date.strftime('%a')  # Get abbreviated weekday name
        current_hour = current_date.hour

        # Check if current_day is in our pairs and if current_hour matches
        if current_day in day_hour_pairs:
            if current_hour in day_hour_pairs[current_day]:
                counts[current_day] += 1

        # Move to the next hour
        current_date += datetime.timedelta(hours=1)

    return counts

# Example usage
start = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

counts = count_day_hour_pairs(start, end, day_hour_pairs)
print(counts)

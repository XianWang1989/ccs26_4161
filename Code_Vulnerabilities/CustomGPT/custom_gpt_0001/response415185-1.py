
import datetime
from collections import defaultdict

def count_day_hour_pairs(start, end, day_hour_pairs):
    # Create a dictionary to hold the count of each (day, hour)
    counts = defaultdict(int)

    # Loop through each day in the range
    current = start
    while current <= end:
        # Get the weekday (0 = Monday, ..., 6 = Sunday)
        weekday = current.strftime("%a")  # This will give 'Mon', 'Tue', etc.

        # If weekday is in the provided pairs, check the hours
        if weekday in day_hour_pairs:
            hour = current.hour
            if hour in day_hour_pairs[weekday]:
                counts[(weekday, hour)] += 1

        # Move to the next day
        current += datetime.timedelta(days=1)

    return counts

# Example usage
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

day_hour_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

counts = count_day_hour_pairs(start, end, day_hour_pairs)

# Print the results
for (day, hour), count in counts.items():
    print(f"{count} occurrences of {day} at {hour}:00.")

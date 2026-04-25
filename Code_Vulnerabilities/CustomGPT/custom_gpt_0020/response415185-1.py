
from datetime import datetime, timedelta

def count_day_hour_pairs(start, end, day_hour_pairs):
    # Initialize a dictionary to hold the counts
    counts = {day: 0 for day in day_hour_pairs}

    # Create a copy of start datetime to iterate
    current = start

    # Loop through each week between start and end
    while current <= end:
        # Get the current day of the week (0=Monday...6=Sunday)
        day_of_week = current.strftime('%a')  # e.g., 'Mon', 'Tue', etc.

        # Check if the current day is in our day_hour_pairs
        if day_of_week in day_hour_pairs:
            # Get the list of hours for that day
            hours = day_hour_pairs[day_of_week]
            # Count occurrences for those hours
            for hour in hours:
                # Check if the current hour matches the desired hour
                if current.hour == hour:
                    counts[day_of_week] += 1

        # Move to the next hour
        current += timedelta(hours=1)

    return counts

# Example usage
day_hour_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

start = datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime(2015, 8, 30, 10, 22, 36, 363912)

result = count_day_hour_pairs(start, end, day_hour_pairs)
print(result)


import datetime
from collections import defaultdict

# Define the day-hour pairs
day_hour_pairs = {
    'Mon': [9, 23],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Thu': [12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Define start and end datetime
start = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

# Function to count hour occurrences for each day-hour pair
def count_day_hour_pairs(start, end, day_hour_pairs):
    counts = defaultdict(int)
    current = start

    # Iterate over each day until the end date is reached
    while current <= end:
        day_name = current.strftime('%a')  # Get day name (e.g., Mon, Tue)

        if day_name in day_hour_pairs:
            for hour in day_hour_pairs[day_name]:
                # Check if the current hour matches the specified hour
                if (current.hour == hour) and (start <= current <= end):
                    counts[(day_name, hour)] += 1

        # Move to the next hour
        if current.hour < 23:
            current += datetime.timedelta(hours=1)
        else:
            # Move to the next day, reset hour to 0
            current = (current + datetime.timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)

    return counts

# Call the function and print the results
counts = count_day_hour_pairs(start, end, day_hour_pairs)
print(dict(counts))

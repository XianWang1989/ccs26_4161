
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

# Define the start and end datetimes
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

def count_day_hour_pairs(start, end, day_hour_pairs):
    # Initialize a count dictionary
    counts = defaultdict(int)

    # Generate the range of dates
    current = start
    while current <= end:
        day_of_week = current.strftime('%a')  # Get the abbreviated day name
        hour = current.hour  # Get the current hour

        # Check if the current day and hour are in the pairs
        if day_of_week in day_hour_pairs and hour in day_hour_pairs[day_of_week]:
            counts[(day_of_week, hour)] += 1

        current += datetime.timedelta(hours=1)  # Increment by one hour

    return counts

# Count the pairs
result = count_day_hour_pairs(start, end, day_hour_pairs)

# Print results
for (day, hour), count in result.items():
    print(f"{day}: {hour} -> {count} occurrence(s)")

# Example for a specific pair
def count_specific_pair(start, end, day, hour):
    count = 0
    current = start
    while current <= end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += datetime.timedelta(hours=1)
    return count

# Count specific pair: Wednesdays at 14
specific_count = count_specific_pair(start, end, 'Wed', 14)
print(f"Wednesdays at 14: {specific_count} occurrence(s)")

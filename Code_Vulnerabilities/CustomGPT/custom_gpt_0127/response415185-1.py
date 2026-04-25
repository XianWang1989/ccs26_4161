
import datetime

# Define the day-of-week-hour pairs
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
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

def count_day_hour_pairs(start, end, pairs):
    current = start
    total_counts = {day: 0 for day in pairs.keys()}

    while current <= end:
        day_name = current.strftime('%a')  # Get the day name (e.g., 'Mon')
        hour = current.hour

        # Check if the current hour is in the corresponding list for the day
        if hour in pairs.get(day_name, []):
            total_counts[day_name] += 1

        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return total_counts

# Count occurrences
result = count_day_hour_pairs(start, end, day_hour_pairs)
print(result)

# Example: Count for Wednesdays at hour 14
def count_specific_day_hour(start, end, day_name, hour):
    current = start
    count = 0

    while current <= end:
        if current.strftime('%a') == day_name and current.hour == hour:
            count += 1
        current += datetime.timedelta(hours=1)

    return count

# Count Wednesdays at hour 14
wednesday_14_count = count_specific_day_hour(start, end, 'Wed', 14)
print(f"Wednesdays at 14: {wednesday_14_count}")

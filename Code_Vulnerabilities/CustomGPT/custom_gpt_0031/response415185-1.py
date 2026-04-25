
from datetime import datetime, timedelta

# The day-hour pairs
time_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Function to count occurrences of day-hour pairs
def count_day_hour_pairs(start, end, pairs):
    current = start
    total_counts = {day: 0 for day in pairs}

    while current <= end:
        day_name = current.strftime('%a')  # Get the day of the week
        if day_name in pairs:
            # Check for each hour if it falls within the start and end range
            for hour in pairs[day_name]:
                # Create a datetime object for that hour
                target_hour = current.replace(hour=hour, minute=0, second=0, microsecond=0)
                if start <= target_hour <= end:
                    total_counts[day_name] += 1
        current += timedelta(days=1)  # Move to the next day

    return total_counts

# Example usage
start = datetime(2015, 7, 22, 17, 58, 54)
end = datetime(2015, 8, 30, 10, 22, 36)

counts = count_day_hour_pairs(start, end, time_pairs)
print(counts)

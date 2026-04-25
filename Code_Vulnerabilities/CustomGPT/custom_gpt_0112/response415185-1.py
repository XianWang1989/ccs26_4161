
from datetime import datetime, timedelta

# Define the day-of-week-hour pairs
time_pairs = {
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

def count_hours(day_hour_pairs, start, end):
    count = 0
    current = start

    # Loop through the days from start to end
    while current <= end:
        day_name = current.strftime('%a')  # Get day name (e.g., 'Mon', 'Tue', etc.)

        # If the current day is in the specified pairs
        if day_name in day_hour_pairs:
            for hour in day_hour_pairs[day_name]:
                # Create a datetime for this hour on the current day
                target_time = current.replace(hour=hour, minute=0, second=0, microsecond=0)
                if start <= target_time <= end:
                    count += 1

        # Move to the next day
        current += timedelta(days=1)

    return count

# Example usage
total_hours = count_hours(time_pairs, start, end)
print(f"Total hours between {start} and {end}: {total_hours}")

# Focusing on a single pair: Wednesdays at 14
def count_specific_hour(day, hour, start, end):
    count = 0
    current = start

    while current <= end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += timedelta(hours=1)

    return count

# Count Wednesdays at 14:00
wednesday_14_count = count_specific_hour('Wed', 14, start, end)
print(f"Total Wednesdays at 14:00: {wednesday_14_count}")

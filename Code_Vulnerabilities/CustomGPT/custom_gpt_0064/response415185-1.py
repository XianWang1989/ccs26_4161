
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

def count_hours_between(start, end, day_hour_pairs):
    total_hours = 0
    current = start

    # Loop through each day in the range
    while current <= end:
        day_name = current.strftime('%a')  # Get the day of the week
        if day_name in day_hour_pairs:
            if day_hour_pairs[day_name]:  # Check if there are hours listed
                for hour in day_hour_pairs[day_name]:
                    hour_start = current.replace(hour=hour, minute=0, second=0, microsecond=0)
                    hour_end = current.replace(hour=hour, minute=59, second=59, microsecond=999999)
                    # Count the valid duration within the given start and end times
                    overlap_start = max(hour_start, start)
                    overlap_end = min(hour_end, end)

                    # If there's an overlap, count the hour
                    if overlap_start <= overlap_end:
                        total_hours += 1
        # Move to the next day
        current += datetime.timedelta(days=1)

    return total_hours

# Example usage
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

result = count_hours_between(start, end, day_hour_pairs)
print(f"Total relevant hours between {start} and {end}: {result}")

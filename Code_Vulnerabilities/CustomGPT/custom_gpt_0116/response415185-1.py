
from datetime import datetime, timedelta

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

# Define the start and end datetime
start = datetime(2015, 7, 22, 17, 58, 54)
end = datetime(2015, 8, 30, 10, 22, 36)

def count_day_hour_pairs(day_hour_pairs, start, end):
    # Count of occurrences
    count = {day: {hour: 0 for hour in hours} for day, hours in day_hour_pairs.items()}

    # Iterate over each day and each hour
    for day, hours in day_hour_pairs.items():
        for hour in hours:
            # Find the first occurrence of 'day' at 'hour' starting from 'start'
            day_start = start + timedelta(days=(7 - start.weekday() + list(day_hour_pairs.keys()).index(day)) % 7)
            target_datetime = day_start.replace(hour=hour, minute=0, second=0, microsecond=0)

            # Count occurrences from target_datetime until end
            while target_datetime <= end:
                if start <= target_datetime <= end:
                    count[day][hour] += 1
                # Move to the next week
                target_datetime += timedelta(weeks=1)

    return count

# Count occurrences
occurrences = count_day_hour_pairs(day_hour_pairs, start, end)
print(occurrences)

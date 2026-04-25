
from datetime import datetime, timedelta

# Define the day-of-week-hour pairs
day_hour_pairs = {
    'Mon': [9, 23],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Thu': [12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

def count_day_hour_pairs(start, end, pairs):
    count_dict = {day: 0 for day in pairs.keys()}
    current = start

    # Iterate through each day in the date range
    while current <= end:
        # Check if it's a weekday to count
        day_name = current.strftime('%a')  # Get the day of the week
        if day_name in pairs:
            # Count the hours
            for hour in pairs[day_name]:
                if current.hour == hour:
                    count_dict[day_name] += 1
        current += timedelta(hours=1)  # Increment hour by hour

    return count_dict

# Define the start and end datetime
start_datetime = datetime(2015, 7, 22, 17, 58, 54)
end_datetime = datetime(2015, 8, 30, 10, 22, 36)

# Count occurrences
result = count_day_hour_pairs(start_datetime, end_datetime, day_hour_pairs)
print(result)

# Example for counting a single pair: Wednesdays at 14
def count_single_day_hour(start, end, day, hour):
    count = 0
    current = start

    while current <= end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += timedelta(hours=1)

    return count

# Count specific pair: Wednesdays at 14
wednesday_count = count_single_day_hour(start_datetime, end_datetime, 'Wed', 14)
print(f'Wednesdays at 14: {wednesday_count}')

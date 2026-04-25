
import datetime

# Define the day-of-week-hour pairs
schedule = {
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

def count_day_hour_pairs(schedule, start, end):
    count = 0

    # Create a mapping for weekdays
    weekday_map = {
        'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3,
        'Fri': 4, 'Sat': 5, 'Sun': 6
    }

    # Iterate over the date range
    current = start
    while current <= end:
        # Check if today is one of the specified days
        day_name = current.strftime('%a')  # Get abbreviated day name
        if day_name in schedule:
            hours = schedule[day_name]

            # Count each hour in the schedule
            for hour in hours:
                # Check if the current hour matches
                if current.hour == hour:
                    count += 1

        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return count

# Count the occurrences
result = count_day_hour_pairs(schedule, start, end)
print(f"Occurrences of specified day-hour pairs: {result}")


import datetime

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

# Define the function to count occurrences
def count_day_hour_pairs(start, end, day_hour_pairs):
    current = start
    count = {day: 0 for day in day_hour_pairs}

    # Iterate over each day in the date range
    while current <= end:
        day_name = current.strftime('%a')  # Get the day of the week
        if day_name in day_hour_pairs:
            for hour in day_hour_pairs[day_name]:
                if current.hour == hour:
                    count[day_name] += 1
        current += datetime.timedelta(hours=1)  # Move to the next hour

    return count

# Define the start and end datetimes
start_time = datetime.datetime(2015, 7, 22, 17, 58, 54)
end_time = datetime.datetime(2015, 8, 30, 10, 22, 36)

# Count occurrences
result = count_day_hour_pairs(start_time, end_time, day_hour_pairs)
print(result)

# Count for specific day-hour pair (Wednesdays: 14)
def count_specific_day_hour(start, end, day, hour):
    count = 0
    current = start
    while current <= end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += datetime.timedelta(hours=1)
    return count

# Example for Wednesdays: 14
wednesday_count_14 = count_specific_day_hour(start_time, end_time, 'Wed', 14)
print(f"Wednesdays at 14: {wednesday_count_14}")

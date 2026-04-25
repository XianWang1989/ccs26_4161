
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

def count_day_hour_pairs(start, end, pairs):
    counts = {day: 0 for day in pairs.keys()}  # Initialize counts
    current = start

    while current <= end:
        day_name = current.strftime('%a')  # Get day of the week
        if day_name in pairs:
            hour = current.hour
            if hour in pairs[day_name]:
                counts[day_name] += 1
        current += datetime.timedelta(hours=1)  # Increment by one hour

    return counts

# Example dates
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

# Count occurrences for all day-hour pairs
result = count_day_hour_pairs(start, end, day_hour_pairs)
print(result)

# Example for counting Wednesdays at 14
def count_specific_day_hour(start, end, day, hour):
    current = start
    count = 0

    while current <= end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += datetime.timedelta(hours=1)  # Increment by one hour

    return count

# Count specific example: Wednesdays at 14
wednesday_14_count = count_specific_day_hour(start, end, 'Wed', 14)
print("Wednesdays at 14:", wednesday_14_count)

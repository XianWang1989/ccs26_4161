
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
    current = start
    count = {day: 0 for day in pairs}  # Initialize a count dictionary

    while current <= end:
        day = current.strftime('%a')  # Get the day abbreviation (Mon, Tue, ...)
        hour = current.hour  # Get the current hour

        if day in pairs and hour in pairs[day]:
            count[day] += 1  # Increment the count for that day-hour pair

        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return count

# Example usage
start_dt = datetime.datetime(2015, 7, 22, 17, 58, 54)
end_dt = datetime.datetime(2015, 8, 30, 10, 22, 36)

result = count_day_hour_pairs(start_dt, end_dt, day_hour_pairs)
print(result)


import datetime

# Define the day-of-week-hour pairs
pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

def count_day_hour_pairs(start, end, pairs):
    count = {day: 0 for day in pairs.keys()}  # Initialize count dictionary

    # Loop through each day in the date range
    current = start
    while current <= end:
        day_name = current.strftime('%a')  # Get the name of the day (Mon, Tue, ...)

        if day_name in pairs:
            hour = current.hour
            # If the current hour is in the specified hours for that day, increase the count
            if hour in pairs[day_name]:
                count[day_name] += 1

        current += datetime.timedelta(hours=1)  # Move to the next hour

    return count

# Specify start and end datetimes
start_date = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end_date = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

# Count the occurrences
result = count_day_hour_pairs(start_date, end_date, pairs)

# Print the result
for day, count in result.items():
    print(f"{day}: {count} hours")

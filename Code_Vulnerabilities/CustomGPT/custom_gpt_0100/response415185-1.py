
import datetime

def count_day_hour_pairs(day_hour_pairs, start, end):
    counts = {}

    # Normalize the start and end datetimes
    start_date = start.date()
    end_date = end.date()

    current_date = start_date

    while current_date <= end_date:
        day_name = current_date.strftime('%a')  # Get the day of the week
        if day_name in day_hour_pairs:
            for hour in day_hour_pairs[day_name]:
                # Check if this hour is within the start and end datetimes
                hour_start = datetime.datetime.combine(current_date, datetime.time(hour))
                hour_end = hour_start + datetime.timedelta(hours=1)

                # Check if hour range overlaps with the given range
                if (hour_end > start) and (hour_start < end):
                    counts[(day_name, hour)] = counts.get((day_name, hour), 0) + 1

        current_date += datetime.timedelta(days=1)

    return counts

# Define your day-hour pairs
day_hour_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Define your datetime range
start = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

# Get counts
result = count_day_hour_pairs(day_hour_pairs, start, end)

# Print the results
for (day, hour), count in result.items():
    print(f"{count} occurrences of {day} at hour {hour} between the two dates.")

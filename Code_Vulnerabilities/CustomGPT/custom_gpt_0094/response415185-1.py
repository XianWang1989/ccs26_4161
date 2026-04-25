
import datetime

# Given day-hour pairs
day_hour_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Start and end datetime
start = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

def count_hours(day_hour_pairs, start, end):
    count = 0
    current_date = start.date()

    while current_date <= end.date():
        day_name = current_date.strftime('%a')  # Get the day of the week
        if day_name in day_hour_pairs:
            hours = day_hour_pairs[day_name]
            for hour in hours:
                # Determine the start and end hour for this day/hour pair
                start_hour = max(start.replace(hour=hour, minute=0, second=0, microsecond=0), current_date)
                end_hour = min(end.replace(hour=hour, minute=59, second=59, microsecond=999999), current_date)

                if start_hour <= end_hour:
                    count += 1

        current_date += datetime.timedelta(days=1)  # Move to the next day

    return count

# Usage example
total_hours = count_hours(day_hour_pairs, start, end)
print("Total valid hours:", total_hours)

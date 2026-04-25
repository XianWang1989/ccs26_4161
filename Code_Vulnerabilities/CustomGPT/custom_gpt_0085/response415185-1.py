
import datetime

# Define your day-hour pairs
day_hour_pairs = {
    'Mon': [9, 23],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Thu': [12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

def count_day_hour_pairs(start, end, day_hour_dict):
    current = start
    total_count = {day: 0 for day in day_hour_dict}

    while current <= end:
        day_name = current.strftime('%a')  # Get the day of the week abbreviation
        if day_name in day_hour_dict:
            for hour in day_hour_dict[day_name]:
                if hour == current.hour:
                    total_count[day_name] += 1
        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return total_count

# Example usage
start_time = datetime.datetime(2015, 7, 22, 17, 58)
end_time = datetime.datetime(2015, 8, 30, 10, 22)

results = count_day_hour_pairs(start_time, end_time, day_hour_pairs)
print(results)

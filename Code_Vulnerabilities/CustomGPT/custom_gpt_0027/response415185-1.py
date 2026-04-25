
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

def count_day_hour_pairs(start_dt, end_dt, schedule):
    count = {day: 0 for day in schedule.keys()}  # Initialize count for each day

    current_dt = start_dt

    while current_dt <= end_dt:
        day_name = current_dt.strftime('%a')  # Get the day of the week (e.g., 'Wed')
        hour = current_dt.hour

        # Check if the current day's hour is in the schedule
        if day_name in schedule and hour in schedule[day_name]:
            count[day_name] += 1

        # Move to the next hour
        current_dt += datetime.timedelta(hours=1)

    return count

# Example usage
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

result = count_day_hour_pairs(start, end, schedule)
print(result)

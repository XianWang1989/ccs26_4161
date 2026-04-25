
from datetime import datetime, timedelta

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

def count_hours(start, end, schedule):
    total_count = {day: 0 for day in schedule.keys()}

    # Iterate through each day in the schedule
    current_day = start
    while current_day <= end:
        day_name = current_day.strftime('%a')
        current_hour = current_day.hour

        # Check if the current day has scheduled hours
        if day_name in schedule:
            for hour in schedule[day_name]:
                if hour == current_hour:
                    total_count[day_name] += 1

        # Move to the next hour
        current_day += timedelta(hours=1)

    return total_count

# Example usage
start = datetime(2015, 7, 22, 17, 58, 54)
end = datetime(2015, 8, 30, 10, 22, 36)
result = count_hours(start, end, schedule)

print(result)

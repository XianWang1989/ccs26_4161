
from datetime import datetime, timedelta

def count_day_hour_pairs(start, end, schedule):
    count = 0
    current = start

    while current <= end:
        day_of_week = current.strftime("%a")  # Get abbreviated weekday name
        hour = current.hour

        # Check if the current day and hour are in the schedule
        if day_of_week in schedule and hour in schedule[day_of_week]:
            count += 1

        # Move to the next hour
        current += timedelta(hours=1)

    return count

# Example usage
start_time = datetime(2015, 7, 22, 17, 58, 54)
end_time = datetime(2015, 8, 30, 10, 22, 36)
schedule = {
    'Mon': [9,23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

result = count_day_hour_pairs(start_time, end_time, schedule)
print(f"Count of specified day-hour pairs: {result}")

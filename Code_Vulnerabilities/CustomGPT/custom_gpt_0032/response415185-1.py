
import datetime

def count_specific_day_hour(start, end, day, hour):
    # Create a mapping of the days of the week
    days_mapping = {
        'Mon': 0,
        'Tue': 1,
        'Wed': 2,
        'Thu': 3,
        'Fri': 4,
        'Sat': 5,
        'Sun': 6
    }

    day_num = days_mapping[day]

    count = 0
    current = start

    # Loop through days until we pass the end date
    while current <= end:
        # Check if current day matches the target day and hour
        if current.weekday() == day_num and current.hour == hour:
            count += 1
        # Move to the next hour
        if current.hour < 23:
            current += datetime.timedelta(hours=1)
        else:
            # Move to the next day at midnight
            current = (current + datetime.timedelta(days=1)).replace(hour=0)

    return count

# Example usage
start_time = datetime.datetime(2015, 7, 22, 17, 58, 54)
end_time = datetime.datetime(2015, 8, 30, 10, 22, 36)
count = count_specific_day_hour(start_time, end_time, 'Wed', 14)

print(f"Count of Wednesdays at 14:00 is: {count}")


from datetime import datetime, timedelta

# Start and End datetime
start = datetime(2015, 7, 22, 17, 58, 54)
end = datetime(2015, 8, 30, 10, 22, 36)

# Function to count specific day-hour occurrences
def count_day_hour(start, end, day, hour):
    count = 0
    current = start

    while current <= end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += timedelta(hours=1)  # Increment by one hour

    return count

# Example usage for Wednesdays at 14 (2 PM)
day = 'Wed'  # Day is given in abbreviated form
hour = 14    # 2 PM in 24-hour format

count = count_day_hour(start, end, day, hour)
print(f"There are {count} occurrences of {day} at {hour}:00 between {start} and {end}.")


from datetime import datetime, timedelta

def count_day_hour(start, end, day, hour):
    count = 0
    current = start

    # Find the first occurrence of the specified day at the specified hour
    while current <= end:
        # Move to the next week if the day doesn't match
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        # Increment by one hour
        current += timedelta(hours=1)

    return count

# Example usage
start_datetime = datetime(2015, 7, 22, 17, 58, 54)
end_datetime = datetime(2015, 8, 30, 10, 22, 36)
day = 'Wed'
hour = 14

result = count_day_hour(start_datetime, end_datetime, day, hour)
print(f"Occurrences of {day} at {hour}:00 between {start_datetime} and {end_datetime}: {result}")

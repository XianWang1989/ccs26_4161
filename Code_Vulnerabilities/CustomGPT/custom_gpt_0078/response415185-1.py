
from datetime import datetime, timedelta

def count_day_hour(start, end, day, hour):
    count = 0
    current = start

    # Move to the first occurrence of the specified day
    while current.weekday() != ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'].index(day):
        current += timedelta(days=1)

    # Count occurrences hour by hour
    while current <= end:
        if current.hour == hour:
            count += 1
        # Move to next hour
        current += timedelta(hours=1)

        # Move to the next day if we surpass 23:59
        if current.hour == 0 and current.minute == 0:
            current += timedelta(days=1)

    return count

# Example usage
start = datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime(2015, 8, 30, 10, 22, 36, 363912)
result = count_day_hour(start, end, 'Wed', 14)
print(f"Occurrences of Wednesdays at 14:00: {result}")

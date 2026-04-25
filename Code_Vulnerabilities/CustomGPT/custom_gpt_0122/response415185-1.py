
import datetime

def count_specific_day_hour(start, end, day, hour):
    # Initialize counter
    count = 0
    # Start from the first occurrence of the specified day
    current = start

    # Find the first occurrence of the specified day
    while current.weekday() != get_weekday_index(day):
        current += datetime.timedelta(days=1)

    # Count occurrences of the specified hour on the specified day
    while current <= end:
        if current.hour == hour:
            count += 1
        current += datetime.timedelta(weeks=1)  # Move to the next week

    return count

def get_weekday_index(day):
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return days.index(day)

# Define start and end datetime
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

# Example usage for "Wednesdays: 14"
count = count_specific_day_hour(start, end, 'Wed', 14)
print(f'Occurrences of Wednesdays at 14:00 between the given dates: {count}')


import datetime

# Define the day-hour pairs
schedule = {
    'Mon': [9, 23],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Thu': [12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': []
}

# Define start and end datetime
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

# Function to count valid hours
def count_valid_hours(start, end, schedule):
    count = 0
    current = start

    while current <= end:
        day_of_week = current.strftime('%a')  # Get the day of the week
        hour = current.hour

        # Check if the current hour is in the schedule for that day
        if day_of_week in schedule and hour in schedule[day_of_week]:
            count += 1

        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return count

# Call the function and print the result
total_hours = count_valid_hours(start, end, schedule)
print(f'Total valid hours: {total_hours}')

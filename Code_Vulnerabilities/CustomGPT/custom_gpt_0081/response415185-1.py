
import datetime

def count_specific_day_hour(start, end, day_of_week, hour):
    # Initialize count
    count = 0

    # Create a timedelta of 1 day
    delta = datetime.timedelta(days=1)

    # Start from the start date
    current = start

    # Loop until current date exceeds end date
    while current <= end:
        # Check if current day is the specific day_of_week and the hour matches
        if current.strftime('%a') == day_of_week and current.hour == hour:
            count += 1
        # Move to the next day
        current += delta

    return count

# Define your start and end datetime objects
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

# Count the occurrences of 'Wednesdays: 14'
number_of_wednesdays_14 = count_specific_day_hour(start, end, 'Wed', 14)
print(f'Number of Wednesdays at 14:00 between the dates: {number_of_wednesdays_14}')

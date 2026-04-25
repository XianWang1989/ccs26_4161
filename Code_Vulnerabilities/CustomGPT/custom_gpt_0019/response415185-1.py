
import datetime

# Define the day-of-week-hour pairs
schedule = {
    'Mon': [9, 23],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Thu': [12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': []
}

def count_hours(start, end, schedule):
    current = start
    count = 0

    # Iterate through each week starting from 'start' to 'end'
    while current < end:
        day_name = current.strftime('%a')  # Get the day of the week
        if day_name in schedule:
            for hour in schedule[day_name]:
                # Create a datetime object for the specific hour
                hour_start = current.replace(hour=hour, minute=0, second=0, microsecond=0)
                hour_end = hour_start + datetime.timedelta(hours=1)

                if hour_start >= end:
                    return count  # Exit if we exceed the end time

                if hour_start >= start and hour_end <= end:
                    count += 1  # Count if the hour falls within the range

        # Move to the next day
        current += datetime.timedelta(days=1)

    return count

# Define the start and end datetime points
start_datetime = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end_datetime = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

# Call the function and print the result
total_hours = count_hours(start_datetime, end_datetime, schedule)
print(f'Total hours for specified day-hour pairs: {total_hours}')

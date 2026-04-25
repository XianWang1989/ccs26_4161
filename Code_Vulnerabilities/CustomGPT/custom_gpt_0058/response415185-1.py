
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

# Define the start and end datetimes
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

def count_hours(schedule, start, end):
    # Create a dictionary to hold counts
    counts = {day: 0 for day in schedule.keys()}

    # Set the current date to the start date
    current_date = start

    # Loop through each day from start to end
    while current_date <= end:
        day_name = current_date.strftime('%a')  # Get the day's name (Mon, Tue, ...)
        if day_name in schedule:
            # Check if the current hour is in the schedule for that day
            current_hour = current_date.hour
            if current_hour in schedule[day_name]:
                counts[day_name] += 1

        # Move to the next hour
        current_date += datetime.timedelta(hours=1)

    return counts

# Count hours for the specified schedule between start and end
result = count_hours(schedule, start, end)

# Print the result
print(result)

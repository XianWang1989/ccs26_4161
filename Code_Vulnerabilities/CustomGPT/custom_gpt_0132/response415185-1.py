
import datetime

# Define the day-of-week-hour pairs
schedule = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Define the start and end datetime
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

# Function to count occurrences for the entire schedule
def count_day_hour_pairs(schedule, start, end):
    count = {day: 0 for day in schedule.keys()}
    current = start

    while current <= end:
        day_name = current.strftime('%a')  # Get the day of the week short name
        hour = current.hour  # Get the current hour

        if day_name in schedule and hour in schedule[day_name]:
            count[day_name] += 1

        # Move to the next hour
        if current.minute == 59:
            current += datetime.timedelta(hours=1, minutes=-59)  # Reset minutes to 0
        else:
            current += datetime.timedelta(minutes=1)  # Move one minute ahead

    return count

# Call the function
result = count_day_hour_pairs(schedule, start, end)
print(result)

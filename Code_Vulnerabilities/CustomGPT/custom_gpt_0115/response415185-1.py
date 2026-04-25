
import datetime
from collections import defaultdict

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

# Start and end datetime
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

def count_day_hour_pairs(schedule, start, end):
    # Create a defaultdict to hold counts for each day
    count = defaultdict(int)

    # Loop through each day in the date range
    current_date = start
    while current_date <= end:
        day_of_week = current_date.strftime('%a')  # Get the day of the week (e.g. 'Mon')

        if day_of_week in schedule:
            current_hour = current_date.hour

            # Check if the current hour is in the schedule for that day
            if current_hour in schedule[day_of_week]:
                count[(day_of_week, current_hour)] += 1

        # Move to the next hour
        current_date += datetime.timedelta(hours=1)

    return count

# Call the function
result = count_day_hour_pairs(schedule, start, end)

# Print the results
for key, value in result.items():
    print(f"{key}: {value}")

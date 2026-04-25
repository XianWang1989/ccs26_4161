
from datetime import datetime, timedelta

# Define the day-of-week-hour pairs
day_hour_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Function to count occurrences of specific day-hour pairs between two dates
def count_day_hour_pairs(start, end, pairs):
    count_dict = {key: 0 for key in pairs.keys()}

    # Create a datetime object for the start of the next week to iterate day by day
    current = start

    # Loop through each date from start to end
    while current <= end:
        day_of_week = current.strftime('%a')  # Get day of the week as abbreviated string

        # Check if the day is in the provided pairs
        if day_of_week in pairs:
            for hour in pairs[day_of_week]:
                if current.hour == hour:  # Check the hour matches
                    count_dict[day_of_week] += 1

        current += timedelta(days=1)  # Move to the next day

    return count_dict

# Start and End datetime
start = datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime(2015, 8, 30, 10, 22, 36, 363912)

# Count occurrences for all pairs
count_result = count_day_hour_pairs(start, end, day_hour_pairs)
print(count_result)

# For a simpler problem, count Wednesdays at hour 14
def count_specific_day_hour(start, end, day, hour):
    count = 0
    current = start
    while current <= end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += timedelta(hours=1)  # Move to the next hour
    return count

# Count Wednesdays at hour 14
wednesday_14_count = count_specific_day_hour(start, end, 'Wed', 14)
print(f"Wednesdays at 14: {wednesday_14_count}")

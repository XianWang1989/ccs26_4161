
import datetime

# Define the day-of-week-hour pairs
time_slots = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Define the start and end datetime
start = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

# Function to count occurrences of day-hour pairs
def count_day_hour_pairs(time_slots, start, end):
    count = 0
    current = start

    while current < end:
        day = current.strftime('%a')  # Get the day of the week
        hour = current.hour            # Get the current hour

        # Check if current day and hour are in the specified pairs
        if day in time_slots and hour in time_slots[day]:
            count += 1

        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return count

# Call the function
total_count = count_day_hour_pairs(time_slots, start, end)
print(f"Total occurrences: {total_count}")

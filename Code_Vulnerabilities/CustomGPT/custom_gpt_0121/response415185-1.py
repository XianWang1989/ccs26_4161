
import datetime

# Define day-hour pairs
day_hour_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Function to count hours for a specific day-hour pair
def count_day_hour(start, end, day, hour):
    current = start
    count = 0

    # Ensure we're operating on the same week for the count
    while current <= end:
        # Check if the current day matches
        if current.strftime('%a') == day and current.hour == hour:
            count += 1

        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return count

# Example usage
start_time = datetime.datetime(2015, 7, 22, 17, 58, 54)
end_time = datetime.datetime(2015, 8, 30, 10, 22, 36)

# Count Wednesdays at hour 14
wednesdays_14_count = count_day_hour(start_time, end_time, 'Wed', 14)
print(f"Number of Wednesdays at 14: {wednesdays_14_count}")

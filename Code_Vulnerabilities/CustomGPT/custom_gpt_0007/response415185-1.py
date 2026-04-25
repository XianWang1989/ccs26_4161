
import datetime

# Define the day-of-week-hour pairs
time_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Define the start and end datetimes
start = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

# Function to count occurrences of day-hour pairs
def count_day_hour_pairs(start, end, pairs):
    total_counts = {day: 0 for day in pairs}
    current_date = start

    while current_date <= end:
        day_name = current_date.strftime('%a')  # Get abbreviated day name (e.g., 'Mon', 'Tue')
        hour = current_date.hour

        # Check if the current day has specified hours to count
        if day_name in pairs:
            if hour in pairs[day_name]:
                total_counts[day_name] += 1

        # Move to the next hour
        current_date += datetime.timedelta(hours=1)

    return total_counts

# Get the counts
counts = count_day_hour_pairs(start, end, time_pairs)

# Print the output
for day, count in counts.items():
    print(f"{day}: {count}")

# Example for a specific day-hour pair (e.g. 'Wed: 14')
def count_specific_day_hour(start, end, day, hour):
    count = 0
    current_date = start

    while current_date <= end:
        if current_date.strftime('%a') == day and current_date.hour == hour:
            count += 1
        current_date += datetime.timedelta(hours=1)

    return count

# Count specific example: Count 'Wednesdays: 14'
specific_count = count_specific_day_hour(start, end, 'Wed', 14)
print(f"Wednesdays at 14: {specific_count}")

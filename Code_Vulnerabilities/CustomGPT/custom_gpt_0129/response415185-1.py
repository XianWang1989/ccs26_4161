
import datetime

def count_day_hour_occurrences(start, end, day, hour):
    # Initialize count
    count = 0

    # Loop through all hours in the date range
    current = start.replace(minute=0, second=0, microsecond=0)

    while current <= end:
        # Check if the current time matches the specified day and hour
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return count

# Define the start and end datetime
start_time = datetime.datetime(2015, 7, 22, 17, 58, 54)
end_time = datetime.datetime(2015, 8, 30, 10, 22, 36)

# Count occurrences of 'Wednesdays at 14:00'
wednesday_14_count = count_day_hour_occurrences(start_time, end_time, 'Wed', 14)
print(f"Occurrences of Wednesdays at 14:00: {wednesday_14_count}")


import datetime

# Function to count specific day-hour occurrences
def count_day_hour(start, end, day, hour):
    # Normalize start time to the beginning of the hour
    start = start.replace(minute=0, second=0, microsecond=0)

    # Initialize the counter
    count = 0

    # Create a timedelta for one hour
    one_hour = datetime.timedelta(hours=1)

    # Loop through each hour from start to end
    while start <= end:
        if start.strftime('%a') == day and start.hour == hour:
            count += 1
        start += one_hour

    return count

# Example usage
start_datetime = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end_datetime = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

# Count Wednesdays at 14:00
day = 'Wed'
hour = 14
result = count_day_hour(start_datetime, end_datetime, day, hour)
print(f"Number of {day}s at {hour}:00 between the two datetimes: {result}")

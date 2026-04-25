
from datetime import datetime, timedelta

def count_day_hour(start, end, day, hour):
    count = 0
    current = start

    # Iterate through each day from start to end
    while current <= end:
        # Check if the current day matches the target day
        if current.strftime('%a') == day:
            # Check if the current hour matches the specified hour
            if current.hour == hour:
                count += 1

        # Move to the next day
        current += timedelta(days=1)

    return count

# Example usage
start = datetime(2015, 7, 22, 17, 58, 54)
end = datetime(2015, 8, 30, 10, 22, 36)
day = 'Wed'
hour = 14

wednesday_count = count_day_hour(start, end, day, hour)
print(f"There are {wednesday_count} occurrences of {day}: {hour} between {start} and {end}.")


from datetime import datetime, timedelta

def count_specific_day_hour(start, end, day, hour):
    # Initialize count
    count = 0

    # Create a timedelta for one day
    one_day = timedelta(days=1)

    # Set the current date to the start date
    current_date = start

    while current_date <= end:
        # Check if the current date's day of the week matches
        if current_date.strftime('%a') == day:
            # Check if the current hour matches
            if current_date.hour == hour:
                count += 1
        # Move to the next hour
        current_date += timedelta(hours=1)

    return count

# Example usage:
start_time = datetime(2015, 7, 22, 17, 58, 54)
end_time = datetime(2015, 8, 30, 10, 22, 36)

# Count how many Wednesdays at 14:00 are between start_time and end_time
wednesday_14_count = count_specific_day_hour(start_time, end_time, 'Wed', 14)
print(f"Count of Wednesdays at 14:00: {wednesday_14_count}")

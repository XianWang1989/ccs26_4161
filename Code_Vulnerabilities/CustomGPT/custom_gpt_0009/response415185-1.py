
import datetime

def count_day_hour_pairs(start_date, end_date, day_of_week, hour):
    current_date = start_date
    count = 0

    # Loop until current date is beyond the end_date
    while current_date <= end_date:
        # Check if the current_date is of the desired day of week and hour
        if current_date.strftime('%A') == day_of_week and current_date.hour == hour:
            count += 1
        # Move to the next hour
        current_date += datetime.timedelta(hours=1)

    return count

# Example usage
start = datetime.datetime(2015, 7, 22, 17, 0)
end = datetime.datetime(2015, 8, 30, 10, 0)

wednesday_count = count_day_hour_pairs(start, end, 'Wednesday', 14)
print(f'Number of Wednesdays at 14: {wednesday_count}')

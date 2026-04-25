
import datetime
import numpy as np

def count_day_hour_pairs(start, end, day_hour_dict):
    # Get total counts for each day-hour pair
    counts = {day: 0 for day in day_hour_dict}

    # Start from the first day of the week of the start date
    current_day = start
    while current_day <= end:
        day_name = current_day.strftime('%a')  # Get day of the week
        if day_name in day_hour_dict:
            # Check the hours for the specific day
            for hour in day_hour_dict[day_name]:
                if current_day.replace(hour=hour) >= start and current_day.replace(hour=hour) <= end:
                    counts[day_name] += 1
        # Move to the next day
        current_day += datetime.timedelta(days=1)

    return counts

# Example usage
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)
day_hour_dict = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

count_results = count_day_hour_pairs(start, end, day_hour_dict)
print(count_results)

# For counting a specific day-hour pair, e.g., Wednesdays at 14
def count_specific_day_hour(start, end, day, hour):
    count = 0
    current_day = start
    while current_day <= end:
        if current_day.strftime('%a') == day and current_day.hour == hour:
            count += 1
        current_day += datetime.timedelta(days=1)
    return count

# Example for Wednesdays at 14
wednesday_14_count = count_specific_day_hour(start, end, 'Wed', 14)
print(f"Wednesdays at 14: {wednesday_14_count}")


import datetime
from collections import defaultdict

# Define the day-hour pairs
day_hour_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

def count_day_hour_pairs(start, end, day_hour_pairs):
    # Create a count dictionary
    counts = defaultdict(int)

    # Generate all days between start and end dates
    current_date = start
    while current_date <= end:
        day_name = current_date.strftime('%a')  # Get day name (Mon, Tue, etc.)
        if day_name in day_hour_pairs:
            for hour in day_hour_pairs[day_name]:
                # Create datetime for current day and hour
                current_hour_date = current_date.replace(hour=hour, minute=0, second=0, microsecond=0)
                if start <= current_hour_date <= end:
                    counts[(day_name, hour)] += 1
        current_date += datetime.timedelta(days=1)

    return counts

# Example usage
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

result = count_day_hour_pairs(start, end, day_hour_pairs)
print(result)

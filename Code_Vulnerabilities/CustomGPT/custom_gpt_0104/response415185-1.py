
from datetime import datetime, timedelta
from collections import defaultdict

def count_day_hour_pairs(start_dt, end_dt, day_hour_map):
    counts = defaultdict(int)

    current_dt = start_dt
    while current_dt <= end_dt:
        day_of_week = current_dt.strftime('%a')  # Get abbreviated day name (e.g., 'Mon')
        hour_of_day = current_dt.hour

        # Check if the current day and hour matches any given pairs
        if day_of_week in day_hour_map and hour_of_day in day_hour_map[day_of_week]:
            counts[(day_of_week, hour_of_day)] += 1

        # Move to the next hour
        current_dt += timedelta(hours=1)

    return counts

# Example usage
start = datetime(2015, 7, 22, 17, 58, 54)
end = datetime(2015, 8, 30, 10, 22, 36)

day_hour_map = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

result = count_day_hour_pairs(start, end, day_hour_map)

print(result)

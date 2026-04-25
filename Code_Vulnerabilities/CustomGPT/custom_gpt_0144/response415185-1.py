from datetime import datetime, timedelta

# Your input data
day_hour_map = {
    'Mon': [9, 23],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Thu': [12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Start and end datetime
start = datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime(2015, 8, 30, 10, 22, 36, 363912)

# Normalize start and end to the nearest hour (rounding down start, up end)
start = start.replace(minute=0, second=0, microsecond=0)
end = (end + timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)

# Mapping of weekday integers to abbreviated names
weekday_map = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# Initialize counts
counts = {day: {hour: 0 for hour in hours} for day, hours in day_hour_map.items()}

# Iterate hour-by-hour
current = start
while current < end:
    day = weekday_map[current.weekday()]
    hour = current.hour
    if hour in day_hour_map.get(day, []):
        counts[day][hour] += 1
    current += timedelta(hours=1)

# Output result
for day in counts:
    for hour in counts[day]:
        print(f"{day} at {hour:02d}:00 — {counts[day][hour]} times")

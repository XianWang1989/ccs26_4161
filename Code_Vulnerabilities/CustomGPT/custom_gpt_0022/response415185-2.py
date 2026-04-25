
def count_specific_pair(start, end, day_name, hour):
    current_time = start
    count = 0
    while current_time <= end:
        if current_time.weekday() == list(day_hour_pairs.keys()).index(day_name) and current_time.hour == hour:
            count += 1
        current_time += datetime.timedelta(hours=1)
    return count

# Count for Wednesdays at hour 14
wednesday_count = count_specific_pair(start_time, end_time, 'Wed', 14)
print(f"Wednesdays at 14: {wednesday_count}")

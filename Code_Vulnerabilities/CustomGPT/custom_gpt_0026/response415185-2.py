
def count_specific_hour(day, hour, start, end):
    occurrences = 0
    current_date = start
    while current_date <= end:
        if current_date.strftime("%a") == day:
            hour_start = current_date.replace(hour=hour, minute=0, second=0, microsecond=0)
            hour_end = current_date.replace(hour=hour + 1, minute=0, second=0, microsecond=0)
            if (hour_start < end) and (hour_end > start):
                occurrences += 1
        current_date += datetime.timedelta(days=1)
    return occurrences

# Count specific hour
wednesday_count = count_specific_hour('Wed', 14, start, end)
print(f"Wednesdays at 14: {wednesday_count}")


def count_single_day_hour(start, end, day, hour):
    count = 0
    current = start

    while current <= end:
        if current.strftime("%a") == day and current.hour == hour:
            count += 1
        current += timedelta(hours=1)

    return count

# Example usage
single_count = count_single_day_hour(start, end, 'Wed', 14)
print(f"Wednesdays at 14: {single_count} occurrences")

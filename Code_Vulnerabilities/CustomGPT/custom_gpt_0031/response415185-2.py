
def count_specific_day_hour(start, end, day, hour):
    current = start
    count = 0

    while current <= end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += timedelta(minutes=1)  # Check every minute

    return count

# Example usage
specific_count = count_specific_day_hour(start, end, 'Wed', 14)
print(specific_count)

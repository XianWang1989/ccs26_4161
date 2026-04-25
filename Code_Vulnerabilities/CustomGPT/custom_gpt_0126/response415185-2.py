
def count_single_pair(start, end, day, hour):
    current = start
    count = 0
    while current <= end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += timedelta(hours=1)
    return count

# Example usage for Wednesday 14:00
wednesday_14_count = count_single_pair(start, end, 'Wed', 14)
print(f"Wednesdays at 14:00 -> {wednesday_14_count} occurrences")

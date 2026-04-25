
def count_specific_day_hour(start_dt, end_dt, day, hour):
    count = 0
    current_dt = start_dt

    while current_dt <= end_dt:
        if current_dt.strftime('%a') == day and current_dt.hour == hour:
            count += 1
        current_dt += datetime.timedelta(hours=1)

    return count

# Example usage for Wednesdays at 14
wednesday_count = count_specific_day_hour(start, end, 'Wed', 14)
print("Wednesdays at 14:", wednesday_count)

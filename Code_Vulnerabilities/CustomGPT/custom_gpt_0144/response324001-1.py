from datetime import datetime

now = datetime.now()
# Convert microseconds to tens of microseconds (i.e., divide by 10)
micro_rounded = round(now.microsecond / 10)

# Format timestamp manually with rounded microseconds
timestamp = now.strftime('%d-%m-%Y %H:%M:%S.') + f'{micro_rounded:05d}'
print(timestamp)

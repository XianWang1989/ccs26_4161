
import csv

# Your data
test = ['item1', '01', '001', 1]

# Manually add quotes for the specific item without causing extra quotes in output
test[1] = '"01"'  # Adding double quotes as a raw string.

# Using the CSV writer
with open('file.txt', 'a', newline='') as file:  # 'a' for append, newline='' to avoid extra newlines
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)  # Use QUOTE_MINIMAL to minimize quotes
    csvOut.writerow(test)

print(test)  # Output: ['item1', '"01"', '001', 1]

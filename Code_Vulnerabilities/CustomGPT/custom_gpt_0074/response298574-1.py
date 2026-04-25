
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add double quotes to the second item
test[1] = '"' + test[1] + '"'

# Open the CSV file for appending
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL, escapechar='\\')
    csvOut.writerow(test)

# Print for verification
print(test)  # Output: ['item1', '"01"', '001', 1]

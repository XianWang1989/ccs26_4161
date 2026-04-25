
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add quotes to the specific item
test[1] = '"{}"'.format(test[1])

# Open the file for appending
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)  # Use QUOTE_NONNUMERIC for non-numeric fields
    csvOut.writerow(test)  # Write the row

print(test)  # Expected output: ['item1', '"01"', '001', 1]

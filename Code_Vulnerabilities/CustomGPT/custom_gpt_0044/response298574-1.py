
import csv

# Test data
test = ['item1', '01', '001', 1]

# Manually add quotes around the desired item
test[1] = '"{}"'.format(test[1])

# Open the CSV file for appending
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)  # Use QUOTE_MINIMAL to avoid extra quotes
    csvOut.writerow(test)

# Print output for verification
print(test)  # Prints: ['item1', '"01"', '001', 1]

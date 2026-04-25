
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add quotes to the required element
test[1] = '"{}"'.format(test[1])

# Print to console for verification
print(test)  # Output: ['item1', '"01"', '001', 1]

# Write to CSV
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

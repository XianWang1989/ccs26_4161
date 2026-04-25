
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add double quotes around the second item
test[1] = '"{}"'.format(test[1])

# Print original list (for verification)
print(test)  # Output: ['item1', '"01"', '001', 1]

# Write to CSV file with custom quoting
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)


import csv

# Test data including a string with quotes
test = ['item1', '01', '001', 1]

# Add double quotes to the second item
test[1] = '"{}"'.format(test[1])

# Open the CSV file in append mode
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)  # Use QUOTE_MINIMAL to avoid extra quotes
    csvOut.writerow(test)  # Write the modified list to the file

# Print output for verification
print(test)  # Output: ['item1', '"01"', '001', 1]


import csv

# Test data
test = ['item1', '01', '001', 1]

# Wrap the second item in quotes
test[1] = '"{}"'.format(test[1])

# Open the output file
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)  # Use QUOTE_MINIMAL to avoid extra quotes
    csvOut.writerow(test)

# Print for verification
print(test)  # prints: ['item1', '"01"', '001', 1]

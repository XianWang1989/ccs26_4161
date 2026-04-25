
import csv

# Test data
test = ['item1', '01', '001', 1]

# Wrap the second item in additional quotes
test[1] = '"{}"'.format(test[1])  # This will create: '"01"'

# Open the output file
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)  # Use QUOTE_MINIMAL
    csvOut.writerow(test)

# Output the list to check
print(test)  # Prints: ['item1', '"01"', '001', 1]

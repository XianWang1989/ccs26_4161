
import csv

# Test data
test = ['item1', '01', '001', 1]

# Manually add double quotes only to specific item
test[1] = '"{}"'.format(test[1])

# Open the CSV file in append mode
with open('file.txt', 'a', newline='') as csvfile:
    csvOut = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# Output the original list for verification
print(test)  # prints: ['item1', '"01"', '001', 1]

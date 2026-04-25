
import csv

# Test data
test = ['item1', '01', '001', 1]

# Manually add double quotes around the second item
test[1] = '"{}"'.format(test[1])

# Write to CSV file
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL, quotechar='"')
    csvOut.writerow(test)

# Print the test data to confirm
print(test)  # This will print: ['item1', '"01"', '001', 1]

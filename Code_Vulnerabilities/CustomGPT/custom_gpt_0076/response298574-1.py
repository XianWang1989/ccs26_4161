
import csv

# Initial test data
test = ['item1', '01', '001', 1]

# Wrap the second item in quotation marks
test[1] = '"{}"'.format(test[1])

# Writing to a CSV file
with open('file.txt', 'a', newline='') as file:  # Use 'newline' parameter for cross-platform compatibility
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL, quotechar='"')
    csvOut.writerow(test)

# Check the content of test list
print(test)  # Expected: ['item1', '"01"', '001', 1]

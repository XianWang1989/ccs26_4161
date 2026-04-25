
import csv

# Test data with quotes
test = ['item1', '01', '001', 1]

# Manually format the second item with double quotes
test[1] = '"{}"'.format(test[1])  # Adds double quotes around '01'

with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# Check output
print(test)  # Should print: ['item1', '"01"', '001', 1]

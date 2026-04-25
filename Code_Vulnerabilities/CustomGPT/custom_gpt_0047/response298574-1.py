
import csv

# Test data
test = ['item1', '01', '001', 1]

# Wrap the desired field with quotes
test[1] = '"{}"'.format(test[1])

# Open a file for appending
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# Print output for verification
print(test)  # Outputs: ['item1', '"01"', '001', 1]

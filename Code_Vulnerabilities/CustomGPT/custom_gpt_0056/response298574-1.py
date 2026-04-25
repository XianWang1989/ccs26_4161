
import csv

# Test data with intentional quotes
test = ['item1', '01', '001', 1]

# Add quotes around the second item
test[1] = '"{}"'.format(test[1])

# Print the modified list
print(test)  # Output: ['item1', '"01"', '001', 1]

# Open CSV file for appending
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# Cleanup
del csvOut

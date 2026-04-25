
import csv

# Test data with quotes
test = ['item1', '01', '001', 1]

# Wrap the specific item in quotes
test[1] = '"{}"'.format(test[1])

with open('file.txt', 'a', newline='') as f:  # Use 'a' mode for appending
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)  # Minimal quoting
    print(test)  # Output: ['item1', '"01"', '001', 1]
    csvOut.writerow(test)  # Writes: item1,"01",001,1

# No need to explicitly delete csvOut, it's handled by context manager

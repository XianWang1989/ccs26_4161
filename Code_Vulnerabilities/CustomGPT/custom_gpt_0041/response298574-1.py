
import csv

# Test data
test = ['item1', '01', '001', 1]

# Adding quotes to the second item only
test[1] = '"'+test[1]+'"'

# Open the output file
with open('file.txt', 'a', newline='') as csvfile:
    csvOut = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)  # Use minimal quoting
    csvOut.writerow(test)

# Print for verification
print(test)  # Should output: ['item1', '"01"', '001', 1]

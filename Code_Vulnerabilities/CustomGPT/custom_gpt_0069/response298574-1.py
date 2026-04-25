
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add double quotes around the second item
test[1] = '01'  # No need to add quotes manually.

# Open the file using 'a' mode to append
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)  # Quote minimally
    print(test)  # Prints: ['item1', '01', '001', 1]
    csvOut.writerow(test)  # Will write: item1,01,001,1

# No need to explicitly delete csvOut as it will be garbage collected.


import csv

# Prepare the test data
test = ['item1', '01', '001', 1]

# Add quotes directly to the specific item
test[1] = '"'+test[1]+'"'

# Open CSV file for appending
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)  # Use QUOTE_MINIMAL to avoid excessive quoting
    csvOut.writerow(test)

# For verification, print to console
print(test)  # Prints: ['item1', '"01"', '001', 1]

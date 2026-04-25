
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add double quotes as a string to the second item
test[1] = '"01"'

# Open the CSV file for appending
with open('file.txt', 'a', newline='') as f:  # Use newline='' to avoid extra newlines
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)  # Use QUOTE_MINIMAL to control quoting
    print(test)  # Expected: ['item1', '"01"', '001', 1]
    csvOut.writerow(test)  # Write the row to the CSV

# No need to explicitly delete the writer object; it will close automatically with 'with'

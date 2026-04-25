
import csv

# test "data"
test = ['item1', '01', '001', 1]

# Manually add quotes around the desired item
test[1] = '"{}"'.format(test[1]) 

# Create CSV writer with appropriate options
with open('file.txt', 'a', newline='') as f:  # Use 'newline=""' for correct new-line handling.
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL, escapechar='\\')  # Adjust quoting as needed
    csvOut.writerow(test)  # Write the row to the CSV file

print(test)  # This will print: ['item1', '"01"', '001', 1]

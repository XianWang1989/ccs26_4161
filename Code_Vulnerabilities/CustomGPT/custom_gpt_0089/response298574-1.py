
import csv

# Test data
test = ['item1', '01', '001', 1]

# Modify the item to have quotes
test[1] = '"' + test[1] + '"'

# Open the CSV file for appending
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)

    # Write the row
    csvOut.writerow(test)

# Print to verify output
print(test)

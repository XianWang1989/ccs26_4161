
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add quotes to the desired element
test[1] = '"{}"'.format(test[1])

# Open the CSV output file
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    # Write the row
    csvOut.writerow(test)

# Verify output
print(test)

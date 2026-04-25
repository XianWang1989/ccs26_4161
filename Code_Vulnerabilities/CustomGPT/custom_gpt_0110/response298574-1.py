
import csv

# Example data
test = ['item1', '01', '001', 1]

# Update the value with double quotes
test[1] = '"' + test[1] + '"'

# Open the file with the correct mode and parameters
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)

    # Write the row
    csvOut.writerow(test)

# Print for confirmation
print(test)

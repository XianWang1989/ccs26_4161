
import csv

# test data
test = ['item1', '01', '001', 1]

# Wrap the second item with double quotes
test[1] = '"' + test[1] + '"'

# Open the file and create a CSV writer with custom quoting
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)

    # Write the row to the output file
    csvOut.writerow(test)

# Print the test data for verification
print(test)  # prints: ['item1', '"01"', '001', 1]

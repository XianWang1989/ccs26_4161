
import csv

# Test data
test = ['item1', '01', '001', 1]

# Format the second item with quotes
test[1] = '"{}"'.format(test[1])

# Open the CSV file in append mode
with open('file.txt', 'a', newline='') as csvfile:
    csvOut = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
    # Write the row to the CSV file
    csvOut.writerow(test)

# Print the output just for verification
print(test)


import csv

# Test data
test = ['item1', '01', '001', 1]

# Add double quotes around the second item
test[1] = '"{}"'.format(test[1])

# Open the CSV file and create a writer object
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)

    # Write the row
    csvOut.writerow(test)

# Print the output for verification
print(test)

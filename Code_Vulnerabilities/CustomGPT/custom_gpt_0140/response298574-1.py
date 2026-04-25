
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add quotes around the second item
test[1] = '"{}"'.format(test[1])

# Open the CSV file for appending
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)

    # Print the modified list
    print(test)  # Prints: ['item1', '"01"', '001', 1]

    # Write the row to the CSV file
    csvOut.writerow(test)

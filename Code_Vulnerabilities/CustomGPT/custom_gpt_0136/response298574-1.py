
import csv

# Test data
test = ['item1', '01', '001', 1]

# Open the CSV file and create a writer
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)

    # Add double quotes around the desired item
    test[1] = '"' + test[1] + '"'

    # Print the modified list
    print(test)  # Output: ['item1', '"01"', '001', 1]

    # Write the row to the CSV file
    csvOut.writerow(test)

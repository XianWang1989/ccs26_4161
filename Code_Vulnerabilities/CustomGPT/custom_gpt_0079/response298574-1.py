
import csv

# Test data
test = ['item1', '01', '001', 1]

# Open the file in append mode
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)

    # Print the original list
    print(test)  # Output: ['item1', '01', '001', 1]

    # Write the row to the CSV file
    csvOut.writerow(test)

# The output in file.txt will be: item1,"01","001",1

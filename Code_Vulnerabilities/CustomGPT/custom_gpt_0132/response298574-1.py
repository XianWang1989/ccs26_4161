
import csv

# Sample data
test = ['item1', '01', '001', 1]

# Setting up the CSV writer
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)

    # Manually adding quotes to the required item
    test[1] = f'"{test[1]}"'

    # Printing the modified test list
    print(test)  # Output: ['item1', '"01"', '001', 1]

    # Writing to the CSV file
    csvOut.writerow(test)

# Cleaning up; no need to explicitly del csvOut

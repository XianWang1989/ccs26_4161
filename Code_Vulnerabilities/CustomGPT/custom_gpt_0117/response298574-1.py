
import csv

# Test data
test = ['item1', '01', '001', 1]

# Manually add quotes to the second item
test[1] = '"01"'

# Open the output file
with open('file.txt', 'a', newline='') as file:
    # Create a CSV writer object with QUOTE_NONE
    csvOut = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar='\\')

    # Print the modified test list
    print(test)  # prints: ['item1', '"01"', '001', 1]

    # Write to CSV
    csvOut.writerow(test)

# No need to explicitly delete csvOut, as it's handled by the context manager.

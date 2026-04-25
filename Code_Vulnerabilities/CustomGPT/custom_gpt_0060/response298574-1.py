
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add quotes to the specific item
test[1] = '"{}"'.format(test[1])

# Open the file in append mode
with open('file.txt', 'a', newline='') as csvfile:
    csvOut = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)  # Use QUOTE_MINIMAL

    # Print the test list to check the output
    print(test)  # Expected: ['item1', '"01"', '001', 1]
    # Write to the output file
    csvOut.writerow(test)

# Clean up
del csvOut

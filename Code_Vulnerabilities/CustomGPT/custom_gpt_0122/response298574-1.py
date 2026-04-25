
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add double quotes to the second item
test[1] = '"{}"'.format(test[1])

# Open the file with appropriate mode
with open('file.txt', 'a', newline='') as file:
    # Create a CSV writer with specific quoting options
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL, quotechar='"')

    # Write the row
    csvOut.writerow(test)

# Printing the result for verification
print(test)  # This will show: ['item1', '"01"', '001', 1]

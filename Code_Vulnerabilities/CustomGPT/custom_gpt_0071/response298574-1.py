
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add quotes to a specific item in the list
test[1] = '"{}"'.format(test[1])

# Open the CSV file
with open('file.txt', 'a', newline='') as csvfile:
    csvOut = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL, quotechar='"')

    # Write the row
    csvOut.writerow(test)

# Check output by printing the list
print(test)

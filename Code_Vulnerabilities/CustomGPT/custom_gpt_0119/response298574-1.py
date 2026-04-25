
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add double quotes to the second item
test[1] = '"{}"'.format(test[1])

# Open the file and create a CSV writer
with open('file.txt', 'a', newline='') as file:
    csv_out = csv.writer(file, quoting=csv.QUOTE_MINIMAL, quotechar='"')

    # Write the row to the file
    csv_out.writerow(test)

# Print the test list to confirm output
print(test)

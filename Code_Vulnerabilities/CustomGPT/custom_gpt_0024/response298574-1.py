
import csv

# Test "data"
test = ['item1', '01', '001', 1]

# Add double quotes explicitly to the specific element you want
test[1] = '"{}"'.format(test[1])

# Open the file for appending
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)

    # Print to verify the content
    print(test)

    # Write the row to the CSV file
    csvOut.writerow(test)

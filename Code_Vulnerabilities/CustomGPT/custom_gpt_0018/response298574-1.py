
import csv

# Initial data
test = ['item1', '01', '001', 1]

# Add quotes to the desired item (without affecting the CSV writer)
test[1] = '"{}"'.format(test[1])  # This will quote the data as you want

# Open the CSV file for appending
with open('file.txt', 'a', newline='') as csvfile:
    csvOut = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)  # Use minimal quoting to avoid extra quotes
    csvOut.writerow(test)  # Write the row to the file

print(test)  # This will print: ['item1', '"01"', '001', 1]

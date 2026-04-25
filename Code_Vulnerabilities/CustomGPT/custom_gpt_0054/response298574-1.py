
import csv

# Initial test data
test = ['item1', '01', '001', 1]

# Add double quotes around the second item
test[1] = '"{}"'.format(test[1])  # This results in '"01"' for our example

# Open the file in append mode
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)  # Use QUOTE_MINIMAL to avoid extra quotes

    # Write the row
    csvOut.writerow(test)

# Print the modified test list
print(test)  # This will output: ['item1', '"01"', '001', 1]

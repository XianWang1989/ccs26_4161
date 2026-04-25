
import csv

# Sample data
test = ['item1', '01', '001', 1]

# Add double quotes to the specific item
test[1] = '"{}"'.format(test[1])  # Wrap '01' in double quotes

# Open the CSV file
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL, quotechar='"')
    csvOut.writerow(test)

# Print the output for verification
print(test)  # Output: ['item1', '"01"', '001', 1]

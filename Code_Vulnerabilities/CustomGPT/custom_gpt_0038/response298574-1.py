
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add double quotes around the second item
test[1] = '"{}"'.format(test[1])

# Print the list to verify
print(test)  # Output: ['item1', '"01"', '001', 1]

# Open the file and write to it
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# Close the writer (handled automatically by 'with')

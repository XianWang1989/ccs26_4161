
import csv

# Sample data
test = ['item1', '01', '001', 1]

# Add double quotes to a specific item in the list
test[1] = '"01"'

# Open the file in append mode
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# Print to check the content
print(test)  # Should print: ['item1', '"01"', '001', 1]

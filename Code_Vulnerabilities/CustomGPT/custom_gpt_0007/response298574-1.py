
import csv

# Initialize your test data
test = ['item1', '01', '001', 1]

# Manually add quotes to the desired elements
# You can retain the original list or change it directly
test[1] = '"{}"'.format(test[1])  # Add quotes to the second item

# Open the file in append mode and write the CSV
with open('file.txt', 'a', newline='') as csvfile:
    csvOut = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)  # Set quoting appropriately
    csvOut.writerow(test)  # Write the row

# Output for debugging
print(test)  # This prints: ['item1', '"01"', '001', 1]

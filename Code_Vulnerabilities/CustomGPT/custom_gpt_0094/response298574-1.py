
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add double quotes to the desired item
test[1] = '"{}"'.format(test[1])

# Print the modified list
print(test)  
# Output: ['item1', '"01"', '001', 1]

# Write to CSV file
with open('file.txt', 'a', newline='') as file:  # Use 'with' to ensure proper closure
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    # Write the row
    csvOut.writerow(test)

# The output file will contain: item1,"01",001,1


import csv

# Example data
test = ['item1', '01', '001', 1]

# Add quotes around the second item
test[1] = '01'  # Use '01' without external quotes

# Create or open the output file in append mode
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)  # Use the MINIMAL quoting option
    # Write the modified test list to the CSV file
    csvOut.writerow(test)

# Output to be printed
print(test)  # This would print: ['item1', '01', '001', 1]

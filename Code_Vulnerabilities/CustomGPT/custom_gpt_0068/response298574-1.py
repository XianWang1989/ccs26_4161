
import csv

# Test data
test = ['item1', '01', '001', 1]

# Modify the item to include quotes
# No need to add quotes manually, we can just keep it as is
test[1] = '01'  # Keep item as '01' (without additional quotes)

# Open the output file with the csv writer
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)  # Use QUOTE_MINIMAL

    # Write the data without additional quotes
    csvOut.writerow(test)

# Now, if you print the contents of the file, it will write as expected.

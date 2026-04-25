
import csv
from io import StringIO

# Test data
test = ['item1', '01', '001', 1]

# Add double quotes to the specific item
test[1] = '"' + test[1] + '"'

# Create a StringIO object to write to temporarily
output = StringIO()
csvOut = csv.writer(output, quoting=csv.QUOTE_MINIMAL)

# Write the row to the StringIO object
csvOut.writerow(test)

# Get the string from StringIO
output_string = output.getvalue()

# Write to the actual file
with open('file.txt', 'a') as f:
    f.write(output_string)

# Clean up
output.close()

# For demonstration, printing what would be in the output file
print(output_string)  # This will show: item1,"01",001,1

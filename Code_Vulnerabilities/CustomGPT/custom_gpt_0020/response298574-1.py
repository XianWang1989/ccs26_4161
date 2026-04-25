
import csv

# Example data
test = ['item1', '01', '001', 1]

# Manually add quotes to the value you want
test[1] = '"{}"'.format(test[1])  # Adds quotes around '01'

# Use csv writer
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)  # Set quoting to QUOTE_MINIMAL
    csvOut.writerow(test)

# Print to validate output in console
print(test)

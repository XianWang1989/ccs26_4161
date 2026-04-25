
import csv

# test "data"
test = ['item1', '01', '001', 1]

# Directly adding the quotes to the string itself
test[1] = '"01"'

# Print the modified list
print(test)  # Output will be: ['item1', '"01"', '001', 1]

with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)  # Use QUOTE_MINIMAL to minimize quoting
    csvOut.writerow(test)

# At this point, if you check 'file.txt', it should write: item1,"01",001,1

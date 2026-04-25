
import csv

# Prepare your data
test = ['item1', '01', '001', 1]

# Instead of adding quotes directly, we will format them when writing
csv_output = csv.writer(open('file.txt', 'a', newline=''), quoting=csv.QUOTE_MINIMAL)

# Modify the second item in the list of test to include quotes when writing
# We're creating a new list for writing, maintaining the original list formatted correctly
formatted_test = [
    test[0], 
    f'"{test[1]}"',  # Use f-string to include quotes around the value
    test[2], 
    test[3]
]

# Printing to see the format
print(formatted_test)  # Output: ['item1', '"01"', '001', 1]

# Write the formatted test to the CSV
csv_output.writerow(formatted_test)

# Clean up
csv_output = None  # Close the CSV writer with None assignment

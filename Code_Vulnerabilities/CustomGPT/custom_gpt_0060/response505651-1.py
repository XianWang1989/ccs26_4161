
lineToWrite = ""

for x in line:
    # Assuming 'x' represents the current company in the list
    if x == 'XXX':  # Check the current company
        continue  # Skip this iteration if 'XXX' is found

    # If 'x' is not 'XXX', append it to lineToWrite
    lineToWrite += x + "\t"  # Add the company with a tab

# Print the final line to check the result
print(lineToWrite)

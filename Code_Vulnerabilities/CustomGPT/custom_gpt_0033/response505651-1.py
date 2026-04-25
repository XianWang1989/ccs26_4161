
lineToWrite = ""

for x in line:
    # Check the current value 'x' instead of 'newCompany'
    if x == 'XXX':
        continue  # Skip this iteration if 'x' is 'XXX'

    # Append the current value to lineToWrite
    lineToWrite += x + "\t"

print(lineToWrite)


lineToWrite = ""

for newCompany in line:
    if newCompany == 'XXX':
        continue  # Skip this iteration if newCompany is 'XXX'
    else:
        lineToWrite += newCompany + "\t"  # Append to the string if not 'XXX'

print(lineToWrite)  # Display the result

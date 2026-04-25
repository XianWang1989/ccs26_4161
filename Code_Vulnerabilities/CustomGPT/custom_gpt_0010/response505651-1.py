
lineToWrite = ""  # Initialize lineToWrite outside the loop

for newCompany in line:  # Loop through each company in the list
    if newCompany == 'XXX':
        continue  # Skip the iteration if company is 'XXX'

    lineToWrite += newCompany + "\t"  # Add the company to lineToWrite

print(lineToWrite)  # Print the result


lineToWrite = ""

for newCompany in line:
    if newCompany == 'XXX':
        continue  # Skip this iteration if the company is 'XXX'

    lineToWrite += newCompany + "\t"  # Append to the line if not 'XXX'

print(lineToWrite)  # Output the result

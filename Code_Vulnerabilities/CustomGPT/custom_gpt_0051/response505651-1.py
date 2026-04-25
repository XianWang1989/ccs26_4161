
line = ['Company1', 'XXX', 'Company2', 'Company3']
lineToWrite = ""

for newCompany in line:
    if newCompany == 'XXX':
        continue  # Skip the iteration if newCompany is 'XXX'

    lineToWrite += newCompany + "\t"  # Otherwise, add to lineToWrite

print(lineToWrite.strip())  # Output the result, removing trailing whitespace

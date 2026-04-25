
line = ['Company1', 'Company2', 'XXX', 'Company4']
lineToWrite = ""

for newCompany in line:
    if newCompany == 'XXX':
        continue  # Skip the rest of the loop for this iteration if company is 'XXX'

    lineToWrite += newCompany + "\t"  # Append valid company to the lineToWrite

print(lineToWrite)

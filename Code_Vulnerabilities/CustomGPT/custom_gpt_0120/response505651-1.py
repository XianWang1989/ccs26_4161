
lineToWrite = ""

for newCompany in line:
    if newCompany == 'XXX':
        continue  # Skip this iteration if Company is 'XXX'

    lineToWrite += newCompany + "\t"

print(lineToWrite)

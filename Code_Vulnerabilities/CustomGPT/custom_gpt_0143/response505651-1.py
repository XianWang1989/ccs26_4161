
lineToWrite = ""

for newCompany in line:
    if newCompany == 'XXX':
        continue
    else:
        lineToWrite += newCompany + "\t"

# Output the result
print(lineToWrite)

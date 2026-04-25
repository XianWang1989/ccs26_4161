
line = ['Company1', 'Company2', 'XXX', 'Company3']
lineToWrite = ""

for newCompany in line:
    if newCompany == 'XXX':
        continue
    else:
        lineToWrite += newCompany + "\t"

print(lineToWrite)

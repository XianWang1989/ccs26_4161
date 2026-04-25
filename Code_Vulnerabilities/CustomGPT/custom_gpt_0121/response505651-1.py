
line = ['Company A', 'Company B', 'XXX', 'Company D']
lineToWrite = ""

for newCompany in line:
    if newCompany == 'XXX':
        continue
    else:
        lineToWrite += newCompany + "\t"

print(lineToWrite)


line = ['Company A', 'XXX', 'Company B', 'Company C']
lineToWrite = ""

for newCompany in line:
    if newCompany == 'XXX':
        continue
    else:
        lineToWrite += newCompany + "\t"

print(lineToWrite.strip())

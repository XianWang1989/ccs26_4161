
line = ['CompanyA', 'CompanyB', 'XXX', 'CompanyD']
lineToWrite = ""

for newCompany in line:
    if newCompany == 'XXX':
        continue
    lineToWrite += newCompany + "\t"

print(lineToWrite)

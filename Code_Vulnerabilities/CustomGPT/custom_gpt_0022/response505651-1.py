
lineToWrite = ""
line = ['CompanyA', 'CompanyB', 'XXX', 'CompanyD']

for newCompany in line:
    if newCompany == 'XXX':
        continue
    else:
        lineToWrite += newCompany + "\t"

print(lineToWrite)

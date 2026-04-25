
line = ['CompanyA', 'XXX', 'CompanyB', 'CompanyC']
lineToWrite = ""

for newCompany in line:
    if newCompany == 'XXX':
        continue
    lineToWrite += newCompany + "\t"

print(lineToWrite.strip())

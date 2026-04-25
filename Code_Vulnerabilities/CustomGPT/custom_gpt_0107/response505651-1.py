
line = ['CompanyA', 'XXX', 'CompanyB', 'CompanyC']
lineToWrite = ""

for newCompany in line:
    if newCompany == 'XXX':
        continue  # Skip this iteration

    lineToWrite += newCompany + "\t"

print(lineToWrite)

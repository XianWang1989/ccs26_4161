
line = ['CompanyA', 'CompanyB', 'XXX', 'CompanyC']
lineToWrite = ""

for newCompany in line:
    if newCompany == 'XXX':
        continue  # Skip this iteration if the company is 'XXX'
    else:
        lineToWrite += newCompany + "\t"

print(lineToWrite)  # Output: CompanyA	CompanyB	CompanyC	

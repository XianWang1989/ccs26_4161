
line = ['CompanyA', 'CompanyB', 'XXX', 'CompanyC']
lineToWrite = ""

for newCompany in line:
    if newCompany == 'XXX':
        continue  # Skip this iteration if newCompany is 'XXX'

    lineToWrite += newCompany + "\t"  # Append the company name

print(lineToWrite)

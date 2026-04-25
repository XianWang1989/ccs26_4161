
line = ['CompanyA', 'CompanyB', 'XXX', 'CompanyC']
lineToWrite = ""

for newCompany in line:
    if newCompany == 'XXX':
        continue  # Skip the iteration if Company is 'XXX'
    else:
        lineToWrite += newCompany + "\t"  # Add the company to lineToWrite

print(lineToWrite.strip())  # Remove the trailing tab

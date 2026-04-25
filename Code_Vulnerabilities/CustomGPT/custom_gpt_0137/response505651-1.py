
line = ['CompanyA', 'CompanyB', 'XXX', 'CompanyC']  # Example list
lineToWrite = ""

for newCompany in line:
    if newCompany == 'XXX':
        continue  # Skip the rest of this iteration if newCompany is 'XXX'
    else:
        lineToWrite += newCompany + "\t"  # Concatenate the company name to lineToWrite

print(lineToWrite)  # Output the written companies

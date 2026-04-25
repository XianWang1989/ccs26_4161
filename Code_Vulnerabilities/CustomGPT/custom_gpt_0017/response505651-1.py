
line = ['CompanyA', 'CompanyB', 'XXX', 'CompanyC']  # Example list
lineToWrite = ""

for newCompany in line:
    if newCompany == 'XXX':
        continue  # Skip this iteration

    lineToWrite += newCompany + "\t"  # Concatenate if condition isn't met

print(lineToWrite)  # Output will be: CompanyA	CompanyB	CompanyC

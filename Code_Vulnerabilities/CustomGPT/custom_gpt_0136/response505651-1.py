
line = ['CompanyA', 'CompanyB', 'XXX', 'CompanyC']  # Example list
lineToWrite = ''

for newCompany in line:
    if newCompany == 'XXX':
        continue  # Skip this iteration if Company is 'XXX'

    lineToWrite += newCompany + "\t"  # Concatenate to lineToWrite

print(lineToWrite)  # Output the result


line = ['CompanyA', 'CompanyB', 'XXX', 'CompanyC', 'CompanyD']  # Sample list of companies
lineToWrite = ""

for newCompany in line:  # Looping through each item in the list
    if newCompany == 'XXX':  # If the company is 'XXX'
        continue  # Skip this iteration

    # If it's not 'XXX', add it to lineToWrite
    lineToWrite += newCompany + "\t"

print(lineToWrite)  # Output the result

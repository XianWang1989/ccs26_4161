
# Assuming 'line' is a list of company names
line = ['CompanyA', 'XXX', 'CompanyB', 'CompanyC']
lineToWrite = ""

for newCompany in line:
    if newCompany == 'XXX':
        continue  # Skip the iteration if the company is 'XXX'

    lineToWrite += newCompany + "\t"  # Concatenate the company name

print(lineToWrite.strip())  # Output the result

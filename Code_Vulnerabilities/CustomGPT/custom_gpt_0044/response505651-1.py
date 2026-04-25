
lines = ['CompanyA', 'CompanyB', 'XXX', 'CompanyC']
lineToWrite = ""

for newCompany in lines:
    if newCompany == 'XXX':
        continue  # Skip the iteration if the company is 'XXX'

    lineToWrite += newCompany + "\t"

print(lineToWrite.strip())  # Output the result

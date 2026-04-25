
lineToWrite = ""

# Example list of companies
companies = ['Company1', 'Company2', 'XXX', 'Company3']

for newCompany in companies:
    if newCompany == 'XXX':
        continue  # Skip this iteration if newCompany is 'XXX'

    lineToWrite += newCompany + "\t"  # Add the company to lineToWrite

# Output the result
print(lineToWrite)

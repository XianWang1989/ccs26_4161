
# Example list of companies
companies = ['ABC', 'XXX', 'DEF', 'XXX', 'GHI']
lineToWrite = ""

for newCompany in companies:
    if newCompany == 'XXX':
        continue  # Skip this iteration if company is 'XXX'

    lineToWrite += newCompany + "\t"  # Add the company to the lineToWrite

print(lineToWrite)  # Output the result

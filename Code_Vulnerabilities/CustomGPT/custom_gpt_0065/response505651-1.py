
lineToWrite = ""

# Sample list of companies
companies = ['ABC', 'XXX', 'DEF', 'XXX', 'GHI']

for newCompany in companies:
    if newCompany == 'XXX':
        continue  # Skip this iteration if the company is 'XXX'

    lineToWrite += newCompany + "\t"  # Append the company to lineToWrite

print(lineToWrite)  # Output will be: ABC    DEF    GHI

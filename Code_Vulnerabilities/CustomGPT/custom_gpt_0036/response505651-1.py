
lineToWrite = ""

# Sample list of companies
companies = ['ABC', 'XXX', 'DEF', 'XXX', 'GHI']

for newCompany in companies:
    if newCompany == 'XXX':
        continue  # Skip this iteration if the company is 'XXX'

    lineToWrite += newCompany + "\t"  # Add the company to lineToWrite if not 'XXX'

print(lineToWrite)  # Output will be: ABC	DEF	GHI

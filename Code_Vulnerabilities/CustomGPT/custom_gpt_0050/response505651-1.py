
lineToWrite = ""

# Sample list of companies
companies = ['ABC', 'DEF', 'XXX', 'GHI']

for newCompany in companies:
    if newCompany == 'XXX':
        continue  # Skip this iteration if newCompany is 'XXX'

    lineToWrite += newCompany + "\t"

print(lineToWrite)

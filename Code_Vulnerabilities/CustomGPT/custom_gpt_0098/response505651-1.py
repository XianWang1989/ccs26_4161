
lineToWrite = ""

# Sample list of companies
companies = ['ABC', 'XXX', 'DEF']

for newCompany in companies:
    if newCompany == 'XXX':
        continue  # Skip the iteration if the company is 'XXX'

    # This block will execute only if newCompany is not 'XXX'
    lineToWrite += newCompany + "\t"

print(lineToWrite)

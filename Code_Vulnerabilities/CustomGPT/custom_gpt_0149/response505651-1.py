
lineToWrite = ""

# Sample list of companies
companies = ['ABC', 'XXX', 'DEF', 'XYZ']

for newCompany in companies:
    if newCompany == 'XXX':
        continue  # Skip this iteration if company is 'XXX'
    else:
        lineToWrite += newCompany + "\t"

print(lineToWrite)

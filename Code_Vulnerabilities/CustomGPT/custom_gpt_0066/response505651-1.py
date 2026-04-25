
lineToWrite = ""

# Sample list of companies
companies = ['ABC', 'XXX', 'DEF', 'XXX', 'GHI']

for newCompany in companies:
    if newCompany == 'XXX':
        continue  # Skip this iteration if newCompany is 'XXX'

    lineToWrite += newCompany + "\t"  # Append to lineToWrite if condition is not met

print(lineToWrite.strip())  # Output the result without trailing tab

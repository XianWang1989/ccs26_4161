
lineToWrite = ""
companies = ['ABC', 'XXX', 'DEF', 'GHI']

for newCompany in companies:
    if newCompany == 'XXX':
        continue  # Skip this iteration if newCompany is 'XXX'

    lineToWrite += newCompany + "\t"  # Concatenate valid company names

print(lineToWrite.strip())  # Output the result, stripping any trailing tab characters

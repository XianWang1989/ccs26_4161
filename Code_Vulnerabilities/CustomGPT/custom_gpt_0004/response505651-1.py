
lineToWrite = ""

# Example list of companies
companies = ['ABC', 'XXX', 'DEF', 'GHI']

for newCompany in companies:
    if newCompany == 'XXX':
        continue  # Skip this iteration if newCompany is 'XXX'

    lineToWrite += newCompany + "\t"  # Add to the lineToWrite if condition is not met

print(lineToWrite)  # Output: ABC   DEF   GHI

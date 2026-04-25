
lineToWrite = ""

# Example list of companies
companies = ['ABC', 'XXX', 'DEF', 'GHI']

for newCompany in companies:
    if newCompany == 'XXX':
        continue  # Skip the iteration if newCompany is 'XXX'

    lineToWrite += newCompany + "\t"  # Append to lineToWrite if condition is not met

print(lineToWrite)  # Output will be: ABC    DEF    GHI    

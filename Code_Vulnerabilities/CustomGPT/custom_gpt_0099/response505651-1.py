
lineToWrite = ""

# Sample list of companies
line = ['ABC', 'XXX', 'DEF', 'GHI']

for newCompany in line:
    if newCompany == 'XXX':
        continue  # Skip this iteration if the company is 'XXX'
    else:
        lineToWrite += newCompany + "\t"

print(lineToWrite)  # Output: ABC    DEF    GHI    

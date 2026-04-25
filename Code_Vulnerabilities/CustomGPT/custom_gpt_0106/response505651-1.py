
# Sample list of companies
companies = ['ABC', 'XXX', 'DEF', 'XXX', 'GHI']
lineToWrite = ""

for newCompany in companies:
    if newCompany == 'XXX':
        continue  # Skip the iteration if the company is 'XXX'

    lineToWrite += newCompany + "\t"  # Append the company to lineToWrite

print(lineToWrite)  # Output: ABC	DEF	GHI	

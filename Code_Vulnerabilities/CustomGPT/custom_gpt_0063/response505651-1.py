
# Example list of companies
companies = ['ABC', 'XXX', 'DEF', 'GHI']

lineToWrite = ""

for newCompany in companies:
    if newCompany == 'XXX':
        continue  # Skip the iteration if newCompany is 'XXX'

    lineToWrite += newCompany + "\t"  # Append the company name to lineToWrite

print(lineToWrite)  # Output will be: ABC	DEF	GHI	

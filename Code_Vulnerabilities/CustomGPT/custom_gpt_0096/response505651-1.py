
# Example list of companies
companies = ['ABC', 'XXX', 'DEF', 'GHI']

lineToWrite = ""

for newCompany in companies:
    if newCompany == 'XXX':
        continue  # Skip 'XXX'

    lineToWrite += newCompany + "\t"  # Append the company name

print(lineToWrite.strip())  # Output the result

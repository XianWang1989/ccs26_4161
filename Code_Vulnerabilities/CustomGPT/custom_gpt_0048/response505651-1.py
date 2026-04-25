
lineToWrite = ""

# Example list of companies
companies = ['AAA', 'XXX', 'BBB', 'CCC']

for newCompany in companies:
    if newCompany == 'XXX':
        continue  # Skip this iteration if the company is 'XXX'

    lineToWrite += newCompany + "\t"  # Add the company to the line

print(lineToWrite)  # Output the result

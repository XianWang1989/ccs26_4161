
line = ['Company A', 'XXX', 'Company B', 'Company C']
lineToWrite = ""

for newCompany in line:
    if newCompany == 'XXX':
        continue  # Skip this iteration if the company is 'XXX'

    lineToWrite += newCompany + "\t"  # Append non-'XXX' companies

print(lineToWrite)  # Output: Company A	Company B	Company C	

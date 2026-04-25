
line = ['Company A', 'Company B', 'XXX', 'Company C']
lineToWrite = ""

for newCompany in line:
    if newCompany == 'XXX':
        continue  # Skip this iteration if the company is 'XXX'

    lineToWrite += newCompany + "\t"  # Append the company to lineToWrite

print(lineToWrite.strip())  # Output the result, stripping any trailing tabs

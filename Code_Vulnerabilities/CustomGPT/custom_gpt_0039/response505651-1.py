
line = ['Company A', 'Company B', 'XXX', 'Company C']
lineToWrite = ""

for newCompany in line:
    if newCompany == 'XXX':
        continue  # Skip this iteration if newCompany is 'XXX'
    else:
        lineToWrite += newCompany + "\t"

print(lineToWrite.strip())  # Output: Company A  Company B  Company C

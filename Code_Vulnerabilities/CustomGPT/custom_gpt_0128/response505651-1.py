
line = ['Company A', 'Company B', 'XXX', 'Company C']  # Example list
lineToWrite = ""

for newCompany in line:
    if newCompany == 'XXX':
        continue  # Skip this iteration if Company is 'XXX'
    else:
        lineToWrite += newCompany + "\t"  # Append the company to lineToWrite

print(lineToWrite)  # Output: Company A    Company B    Company C

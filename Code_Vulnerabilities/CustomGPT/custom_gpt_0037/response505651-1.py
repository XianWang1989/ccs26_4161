
line = ['ABC', 'XXX', 'DEF', 'GHI']
lineToWrite = ""

for newCompany in line:
    if newCompany == 'XXX':
        continue  # Skip this iteration if the company is 'XXX'
    else:
        lineToWrite += newCompany + "\t"  # Add the company to the lineToWrite

print(lineToWrite.strip())  # Output the result without trailing tab

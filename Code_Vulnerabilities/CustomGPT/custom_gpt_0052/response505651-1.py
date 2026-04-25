
line = ['Company_A', 'XXX', 'Company_B', 'Company_C']
lineToWrite = ""

for newCompany in line:
    if newCompany == 'XXX':
        continue  # Skip this iteration if newCompany is 'XXX'

    lineToWrite += newCompany + "\t"

print(lineToWrite.strip())  # Print the result without trailing tab

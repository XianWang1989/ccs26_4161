
lineToWrite = ""

for newCompany in line:  # assuming line is your list
    if newCompany == 'XXX':
        continue  # Skip this iteration if newCompany is 'XXX'

    # This part executes only if newCompany is not 'XXX'
    lineToWrite += newCompany + "\t"

print(lineToWrite)  # You can print or use lineToWrite as needed

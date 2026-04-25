
lineToWrite = ""

for x in line:
    newCompany = x  # Assuming x represents the company name in your list
    if newCompany == 'XXX':
        continue  # Skip this iteration if the company is 'XXX'

    lineToWrite += newCompany + "\t"  # Add the company name to lineToWrite

print(lineToWrite)

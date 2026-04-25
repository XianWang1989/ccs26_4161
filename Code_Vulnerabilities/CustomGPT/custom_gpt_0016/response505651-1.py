
lineToWrite = ""

# Assuming `line` is your list of companies
for newCompany in line:
    if newCompany == 'XXX':
        continue  # Skip the iteration if newCompany is 'XXX'

    lineToWrite += newCompany + "\t"  # Append the company name to lineToWrite

print(lineToWrite)  # Output the result

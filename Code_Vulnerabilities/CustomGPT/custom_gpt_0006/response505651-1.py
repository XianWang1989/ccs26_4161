
line = ['ABC', 'XXX', 'DEF', 'XXX', 'GHI']
lineToWrite = ""

for newCompany in line:
    if newCompany == 'XXX':
        continue  # Skip this iteration if newCompany is 'XXX'

    lineToWrite += newCompany + "\t"  # Append valid companies

# Output the result
print(lineToWrite.strip())

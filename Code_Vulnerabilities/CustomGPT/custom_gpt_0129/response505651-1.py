
lineToWrite = ""

# Assuming 'line' is a list of companies
line = ['ABC', 'XXX', 'DEF', 'XXX', 'GHI']

for newCompany in line:
    if newCompany == 'XXX':
        continue  # Skip this iteration if newCompany is 'XXX'

    # This part runs only if newCompany is not 'XXX'
    lineToWrite += newCompany + "\t"

print(lineToWrite)  # Output will be: "ABC\tDEF\tGHI\t"

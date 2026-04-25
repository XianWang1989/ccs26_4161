
# Sample list of companies
companies = ['ABC', 'XXX', 'DEF', 'GHI']

# Variable to hold the result
lineToWrite = ""

# Loop through each company
for newCompany in companies:
    if newCompany == 'XXX':
        continue  # Skip iteration if the company is 'XXX'
    else:
        lineToWrite += newCompany + "\t"  # Add company to the string

print(lineToWrite)  # Output should be 'ABC\tDEF\tGHI\t' (without 'XXX')

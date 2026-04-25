
lineToWrite = ""

# Example list of companies
companies = ['ABC', 'XXX', 'DEF', 'GHI']

for newCompany in companies:
    if newCompany == 'XXX':  # Check if newCompany is 'XXX'
        continue  # Skip the rest of the loop for this iteration
    else:
        lineToWrite += newCompany + "\t"  # Append to lineToWrite if condition is not met

print(lineToWrite)

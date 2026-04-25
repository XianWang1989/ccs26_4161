
# Example list of companies
companies = ['ABC', 'XXX', 'DEF', 'GHI']
lineToWrite = ""

for company in companies:
    if company == 'XXX':
        continue  # Skip this iteration if the company is 'XXX'

    lineToWrite += company + "\t"  # Add company to lineToWrite

print(lineToWrite)  # Output should be: ABC    DEF    GHI

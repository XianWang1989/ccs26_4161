
lineToWrite = ""

# Example list of companies
companies = ['ABC', 'XXX', 'DEF', 'XXX', 'GHI']

for company in companies:
    if company == 'XXX':
        continue  # Skip this iteration if the company is 'XXX'
    else:
        lineToWrite += company + "\t"  # Append the company to the output string

print(lineToWrite)  # This will print: ABC    DEF    GHI

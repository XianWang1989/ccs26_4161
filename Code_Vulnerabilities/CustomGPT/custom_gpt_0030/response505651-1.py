
# Sample list of companies
companies = ['ABC', 'XXX', 'DEF', 'GHI']

# Variable to store the output
lineToWrite = ""

# Loop through the list of companies
for company in companies:
    # Skip iteration if the company is 'XXX'
    if company == 'XXX':
        continue
    else:
        lineToWrite += company + "\t"

# Print the resulting string
print(lineToWrite)

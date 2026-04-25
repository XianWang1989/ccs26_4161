
# Sample list of companies
companies = ['ABC Corp', 'DEF Inc', 'XXX', 'GHI Ltd']

# Initialize an empty string to accumulate lines to write
lineToWrite = ""

# Loop through each company in the list
for newCompany in companies:
    if newCompany == 'XXX':
        continue  # Skip this iteration if the company is 'XXX'

    # Append the company name with a tab character
    lineToWrite += newCompany + "\t"

# Print the resulting line
print(lineToWrite)

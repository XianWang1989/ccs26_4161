
# Example list of companies
companies = ['ABC', 'XXX', 'DEF', 'GHI']

# Initialize an empty string to store the result
lineToWrite = ""

for newCompany in companies:
    # Check if the company is 'XXX'
    if newCompany == 'XXX':
        continue  # Skip this iteration

    # Add the company to the lineToWrite string
    lineToWrite += newCompany + "\t"

print(lineToWrite)  # Output: ABC	DEF	GHI	

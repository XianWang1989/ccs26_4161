
# Sample list of companies
companies = ['ABC', 'XXX', 'DEF', 'GHI']

# Initialize an empty string to store the results
lineToWrite = ""

# Loop through each company in the list
for newCompany in companies:
    # If newCompany is 'XXX', skip this iteration
    if newCompany == 'XXX':
        continue
    else:
        # Append the company to lineToWrite if the condition is not met
        lineToWrite += newCompany + "\t"

# Print the result
print(lineToWrite.strip())  # Output: ABC    DEF    GHI

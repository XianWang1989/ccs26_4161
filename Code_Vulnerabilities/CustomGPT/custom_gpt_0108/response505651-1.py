
# Sample list of companies
companies = ["ABC", "XXX", "DEF", "XYZ"]

# Initialize an empty string to accumulate results
lineToWrite = ""

# Loop through the list of companies
for newCompany in companies:
    if newCompany == 'XXX':
        continue  # Skip this iteration if the company is 'XXX'
    else:
        lineToWrite += newCompany + "\t"  # Add company name to the output string

# Print the result
print(lineToWrite)

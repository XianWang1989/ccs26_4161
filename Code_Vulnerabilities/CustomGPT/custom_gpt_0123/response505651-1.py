
lineToWrite = ""

# Example list of companies
line = ['CompanyA', 'CompanyB', 'XXX', 'CompanyC']

for x in line:
    if x == 'XXX':
        continue  # Skip this iteration if the company is 'XXX'

    lineToWrite += x + "\t"  # Add company to lineToWrite if not 'XXX'

# Print the result
print(lineToWrite.strip())  # Output will not include 'XXX'

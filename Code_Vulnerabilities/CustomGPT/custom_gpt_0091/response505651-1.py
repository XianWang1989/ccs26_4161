
# Example list of companies
companies = ['ABC', 'XXX', 'DEF', 'GHI', 'XXX', 'JKL']

lineToWrite = ""

for newCompany in companies:
    if newCompany == 'XXX':
        continue  # Skip the rest of the loop for this iteration

    # This part will run only if newCompany is not 'XXX'
    lineToWrite += newCompany + "\t"

print(lineToWrite.strip())  # Output the result, trimmed of extra tabs

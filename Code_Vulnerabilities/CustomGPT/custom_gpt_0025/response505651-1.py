
# Sample list of companies
companies = ['ABC', 'XXX', 'DEF', 'XXX', 'GHI']
lineToWrite = ""

for company in companies:
    if company == 'XXX':
        continue  # Skip this iteration if the company is 'XXX'

    lineToWrite += company + "\t"  # Append the company to lineToWrite

print(lineToWrite.strip())  # Print the result, stripped of trailing tabs

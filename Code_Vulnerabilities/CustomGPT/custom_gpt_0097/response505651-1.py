
lineToWrite = ""
companies = ['ABC', 'XXX', 'DEF', 'GHI']

for company in companies:
    if company == 'XXX':
        continue  # Skip this iteration if company is 'XXX'

    lineToWrite += company + "\t"  # Concatenate valid companies

print(lineToWrite.strip())  # Output the result

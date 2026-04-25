
companies = ['ABC', 'XXX', 'DEF', 'XXX', 'GHI']
lineToWrite = ""

for company in companies:
    if company == 'XXX':
        continue  # Skip this iteration if the company is 'XXX'
    else:
        lineToWrite += company + "\t"

print(lineToWrite)

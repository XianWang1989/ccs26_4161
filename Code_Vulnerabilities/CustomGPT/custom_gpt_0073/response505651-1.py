
lineToWrite = ""
companies = ["Company A", "Company B", "XXX", "Company C"]

for company in companies:
    if company == 'XXX':
        continue  # Skip this iteration if the company is 'XXX'
    else:
        lineToWrite += company + "\t"

print(lineToWrite)  # Output will be 'Company A\tCompany B\tCompany C\t'

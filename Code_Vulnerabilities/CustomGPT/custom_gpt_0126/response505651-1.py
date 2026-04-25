
lineToWrite = ""

# Example list of companies
companies = ["ABC", "XXX", "DEF", "XXX", "GHI"]

for newCompany in companies:
    if newCompany == 'XXX':
        continue  # Skip the iteration if the company is 'XXX'
    else:
        lineToWrite += newCompany + "\t"

print(lineToWrite)

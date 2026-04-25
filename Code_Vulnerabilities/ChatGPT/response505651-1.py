
line = ['Company A', 'Company B', 'XXX', 'Company D']  # Example list of companies
lineToWrite = ""  # Initialize an empty string to store the result

for newCompany in line:  # Iterate through the list of companies
    if newCompany == 'XXX':  # Check if the current company is 'XXX'
        continue  # Skip to the next iteration if the condition is met
    else:
        lineToWrite += newCompany + "\t"  # Append the company to lineToWrite

print(lineToWrite.strip())  # Print the result, removing any trailing whitespace


lineToWrite = ""  # Initialize the variable to store the result
companies = ["ABC", "XXX", "DEF"]  # Example list of companies

for company in companies:
    if company == 'XXX':
        continue  # Skip the iteration if the company is 'XXX'

    lineToWrite += company + "\t"  # Append the company to the lineToWrite

print(lineToWrite)  # Output the result

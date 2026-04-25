
while True:  # Start of the loop
    try:
        NumOfPpl = raw_input('Enter the number of people: ')  # Prompt for input
        NumOfPpl = int(NumOfPpl)  # Attempt to convert to integer
        break  # Exit loop if conversion is successful
    except ValueError:
        print("\nPlease make sure you key in number only! \n\tand please do not leave blank!")

print("\nIs there any of these person present?: \n\tA. Disabled \n\tB. 65-years-old and above \n\tC. None for both A. and B. \n")

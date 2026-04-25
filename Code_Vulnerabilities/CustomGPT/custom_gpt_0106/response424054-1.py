
while True:  # Infinite loop for input validation
    try:
        NumOfPpl = raw_input('Enter the number of people: ')  # Input
        NumOfPpl = int(NumOfPpl)  # Convert to integer
        break  # Exit loop if input is valid
    except ValueError:
        print("\nPlease make sure you key in number only! \n\tand please do not leave blank!")

print("\nIs there any of these persons present?: ")
print("\tA. Disabled ")
print("\tB. 65-years-old and above ")
print("\tC. None for both A. and B.")

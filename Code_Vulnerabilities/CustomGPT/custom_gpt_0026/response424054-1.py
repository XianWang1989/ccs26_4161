
while True:  # Start looping
    try:
        NumOfPpl = input('Enter the number of people: ')  # Get user input
        NumOfPpl = int(NumOfPpl)  # Convert to integer
        break  # Exit if valid
    except ValueError:
        print("\nPlease make sure you key in number only!\n\tand please do not leave blank!")

print("\nIs there any of these person present?:")
print("\tA. Disabled")
print("\tB. 65-years-old and above")
print("\tC. None for Both A. and B.")

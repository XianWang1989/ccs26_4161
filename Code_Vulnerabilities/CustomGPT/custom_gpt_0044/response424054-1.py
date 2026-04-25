
while True:  # Loop until a valid number is entered
    try:
        NumOfPpl = input('Enter the number of people: ')  # Prompt user
        NumOfPpl = int(NumOfPpl)  # Convert input to integer
        break  # Exit loop if conversion is successful
    except ValueError:
        print("\nPlease make sure you key in number only! \n\tand please do not leave blank!")

print("\nIs there any of these persons present?:")
print("\tA. Disabled")
print("\tB. 65-years-old and above")
print("\tC. None for Both A. and B.")

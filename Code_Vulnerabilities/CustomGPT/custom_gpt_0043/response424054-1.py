
while True:  # start the looping process
    try:
        NumOfPpl = input('Enter the number of people: ')  # Prompt the user
        NumOfPpl = int(NumOfPpl)  # Convert input to integer
        break  # Exit loop if conversion is successful
    except ValueError:
        print("\nPlease make sure you key in number only! \n\tand please do not leave blank!")  # Error message

print("\nIs there any of these persons present?: \n\tA. Disabled \n\tB. 65-years-old and above \n\tC. None for Both A. and B. \n")

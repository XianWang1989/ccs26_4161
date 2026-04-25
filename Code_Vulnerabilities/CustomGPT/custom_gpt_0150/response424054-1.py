
while True:  # Infinite loop for input
    try:
        NumOfPpl = input('Enter the number of people: ')  # Changed to input() for Python 3
        NumOfPpl = int(NumOfPpl)
        break  # Exit the loop if the input is valid
    except ValueError:
        print("\nPlease make sure you key in number only! \n\tand please do not leave blank!")

print("\nIs there any of these persons present?: \n\tA. Disabled \n\tB. 65-years-old and above \n\tC. None for Both A. and B.")

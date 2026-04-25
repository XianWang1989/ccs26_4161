
while True:  # Infinite loop until break
    try:
        NumOfPpl = input('Enter the number of people: ')  # Use input() for Python 3
        NumOfPpl = int(NumOfPpl)  # Convert input to an integer
        break  # Exit the loop if conversion is successful
    except ValueError:  # Catch any ValueError exception
        print("\nPlease make sure you key in number only! \n\tand please do not leave blank!")

print("\nIs there any of these persons present?: \n\tA. Disabled \n\tB. 65-years-old and above \n\tC. None for Both A. and B. \n")


while True:  # Exception loop
    try:
        NumOfPpl = input('Enter the number of people: ')  # use input instead of raw_input in Python 3
        NumOfPpl = int(NumOfPpl)
        break  # Exit the loop if the number is valid
    except ValueError:
        print("\nPlease make sure you key in number only! \n\tand please do not leave blank!")

print("\nIs there any of these persons present?: \n\tA. Disabled \n\tB. 65-years-old and above \n\tC. None for Both A. and B. \n")

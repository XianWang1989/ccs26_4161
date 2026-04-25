
while True:  # Exception loop
    try:
        NumOfPpl = input('Enter the number of people: ')  # Use input instead of raw_input for Python 3
        NumOfPpl = int(NumOfPpl)
        break  # Exit loop if input is valid
    except ValueError:
        print("\nPlease make sure you input a number only! \n\tand please do not leave blank!")

print("\nIs there any of these persons present?: \n\tA. Disabled \n\tB. 65-years-old and above \n\tC. None for Both A and B \n")

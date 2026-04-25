
while True:  # exception loop
    try:
        NumOfPpl = input('Enter the number of people: ')  # Change raw_input to input for Python 3
        NumOfPpl = int(NumOfPpl)
        break  # Exit if Conversion to integer is successful
    except ValueError:
        print("\nPlease make sure you key in number only!\n\tand please do not leave blank!")

print("\nIs there any of these persons present?\n\tA. Disabled\n\tB. 65-years-old and above\n\tC. None for Both A. and B.\n")

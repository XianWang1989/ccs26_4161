
while True:  # exception loop
    try:
        NumOfPpl = input('Enter the number of people: ')  # use input() in Python 3
        NumOfPpl = int(NumOfPpl)  # converts to integer
        break  # exit the loop if num is an integer
    except ValueError:
        print("\nPlease make sure you key in a number only! \n\tand please do not leave blank!")

print("\nIs there any of these persons present?: \n\tA. Disabled \n\tB. 65-years-old and above \n\tC. None for Both A and B.")

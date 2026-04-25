
while True:
    try:
        NumOfPpl = input('Enter the number of people: ')
        NumOfPpl = int(NumOfPpl)
        break
    except ValueError:
        print("\nPlease make sure you key in number only! \n\tand please do not leave blank!")

print("\nIs there any of these person present?: \n\tA. Disabled \n\tB. 65-years-old and above \n\tC. None for Both A. and B. \n")


while True:
    try:
        NumOfPpl = int(input('Enter the number of people: '))
        break  # Exit the loop if input is an integer
    except ValueError:
        print("\nPlease make sure you key in numbers only! \n\tand please do not leave blank!")

print("\nIs there any of these persons present?: \n\tA. Disabled \n\tB. 65-years-old and above \n\tC. None for Both A. and B.")

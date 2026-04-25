
while True:  # Start of do-while loop
    try:
        num_of_people = input('Enter the number of people: ')  # Change raw_input to input (Python 3)
        num_of_people = int(num_of_people)  # Attempt to convert to integer
        break  # Exit loop if input is valid
    except ValueError:
        print("\nPlease make sure you key in number only! \n\tand please do not leave blank!")

print("\nIs there any of these person present?: \n\tA. Disabled \n\tB. 65-years-old and above \n\tC. None for Both A. and B.")

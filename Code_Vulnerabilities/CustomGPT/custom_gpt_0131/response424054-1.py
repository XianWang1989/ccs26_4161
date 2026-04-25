
while True:  # Infinite loop
    try:
        NumOfPpl = raw_input('Enter the number of people: ')
        NumOfPpl = int(NumOfPpl)  # Convert input to integer
        break  # Exit loop if input is valid
    except ValueError:
        print("\nPlease make sure you key in number only! \n\tand please do not leave blank!")

print("\nIs there any of these persons present?: \n\tA. Disabled \n\tB. 65-years-old and above \n\tC. None for Both A. and B.")

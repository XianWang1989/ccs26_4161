
while True:  # Infinite loop
    try:
        NumOfPpl = input('Enter the number of people: ')  # 'raw_input' for Python 2, use 'input' for Python 3
        NumOfPpl = int(NumOfPpl)  # Convert to integer
        break  # Exit loop if conversion is successful
    except ValueError:
        print("\nPlease make sure you key in number only! \n\tand please do not leave blank!")

print("\nIs there any of these persons present?: \n\tA. Disabled \n\tB. 65-years-old and above \n\tC. None for both A. and B.")

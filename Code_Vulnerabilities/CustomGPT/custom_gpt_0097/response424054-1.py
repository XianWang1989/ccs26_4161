
# Start the exception loop
while True:
    try:
        # Prompt the user for number of people
        NumOfPpl = input('Enter the number of people: ')  # Use input() for Python 3
        NumOfPpl = int(NumOfPpl)  # Convert to integer
        break  # Exit loop if input is valid
    except ValueError:
        print("\nPlease make sure you key in number only! \n\tand please do not leave blank!")

# Ask about the presence of specific individuals
print("\nIs there any of these persons present?: \n\tA. Disabled \n\tB. 65 years old and above \n\tC. None for both A and B\n")

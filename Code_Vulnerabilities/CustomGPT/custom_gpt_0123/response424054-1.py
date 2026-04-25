
while True:  # Exception loop
    try:
        NumOfPpl = int(input('Enter the number of people: '))  # Using input instead of raw_input
        break  # Exit loop if num is an integer
    except ValueError:
        print("\nPlease make sure you key in number only! \n\tand please do not leave blank!")

print("\nIs there any of these persons present?:\n\tA. Disabled\n\tB. 65-years-old and above\n\tC. None for both A and B\n")

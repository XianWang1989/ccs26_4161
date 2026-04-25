
def Help():
    while True:
        # Prompt the user for input
        print('The options available are: \n')
        print('Intent')
        print('Manifest')
        print('Type Q to Quit \n')

        x = input('What option do you choose: ')
        print('\n')

        if x == 'Q':
            break  # Exit the loop
        elif x == 'Manifest':
            return Manifest()  # Call Manifest function
        elif x == 'Intent':
            return Intent()  # Call Intent function
        else:
            print("Invalid option. Please try again.")

def Manifest():
    return "You chose Manifest!"

def Intent():
    return "You chose Intent!"

# Start the help function to prompt the user
result = Help()
print(result)

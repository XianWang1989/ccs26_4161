
def Help():
    while True:
        string = input('What option do you choose (Manifest/Intent)? \nType Q to Quit: ')
        print('\n')
        if string == 'Manifest':
            return Manifest()
        elif string == 'Intent':
            return Intent()
        elif string == 'Q':
            break
        else:
            print('The options available are: \n')
            for i in andHelp:
                print(i)
            print('Please choose again.\n')

# Define your Manifest and Intent functions
def Manifest():
    print("You've chosen Manifest!")
    # Add your Manifest functionality here

def Intent():
    print("You've chosen Intent!")
    # Add your Intent functionality here

# Call the Help function to start
Help()


def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()
        elif string == 'Intent':
            return Intent()
        else:
            print('The options available are:')
            for i in andHelp:
                print(i)
            print('Type Q to Quit')
            x = input('What option do you choose: ')
            print('\n')
            if x == 'Q':
                break
            else:
                # Directly update the string variable and continue the loop
                string = x

# Example implementations of Manifest and Intent
def Manifest():
    print("Manifest function called.")

def Intent():
    print("Intent function called.")

# List to demonstrate available options
andHelp = ['Intent', 'Manifest']

# Initial call to the function
Help('')  # Starting with an empty string

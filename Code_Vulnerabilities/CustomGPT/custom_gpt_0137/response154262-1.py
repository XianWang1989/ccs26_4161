
def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()  # Call your Manifest function here.
        elif string == 'Intent':
            return Intent()  # Call your Intent function here.
        else:
            print('The options available are: \n')
            for i in andHelp:
                print(i)
            print('Type Q to Quit \n')

            x = input('What option do you choose: ')
            print('\n')
            if x == 'Q':
                break
            else:
                string = x  # Update the string to the new input for the next iteration of the loop.

# Example usage
andHelp = ["Intent", "Manifest"]

def Manifest():
    return "Called Manifest function."

def Intent():
    return "Called Intent function."

# Start the Help function
Help("Start")

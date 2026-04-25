
def Help(string):
    while True:
        # Check provided option
        if string == 'Manifest':
            return Manifest()  # Call Manifest function
        elif string == 'Intent':
            return Intent()  # Call Intent function
        else:
            print('The options available are: \n')
            for i in andHelp:  # Assuming 'andHelp' is defined somewhere
                print(i)
            print('Type Q to Quit \n')
            x = input('What option do you choose: ')
            print('\n')
            # Check if user wants to quit
            if x == 'Q':
                break
            else:
                # Instead of calling Help recursively, assign the input to 'string'
                string = x

# Example usage; simulate the function call with an input
andHelp = ["Manifest", "Intent"]
Help("InvalidInput")  # Start with an invalid input

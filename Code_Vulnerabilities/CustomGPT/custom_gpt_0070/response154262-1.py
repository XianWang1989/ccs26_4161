
def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()  # Ends the function successfully
        elif string == 'Intent':
            return Intent()  # Ends the function successfully
        else:
            print('The options available are: \n')
            for i in andHelp:
                print(i)
            print('Type Q to Quit \n')
            x = input('What option do you choose: ')
            print('\n')
            if x == 'Q':
                break  # Breaks the loop if Q is chosen
            else:
                string = x  # Update the string to the new input to continue the loop

# Example usage
andHelp = ['Intent', 'Manifest']

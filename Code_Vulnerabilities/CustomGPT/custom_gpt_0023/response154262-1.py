
def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()
        elif string == 'Intent':
            return Intent()
        else:
            print('The options available are: \n')
            for i in andHelp:
                print(i)
            print('Type Q to Quit \n')
            x = input('What option do you choose: ')
            print('\n')
            if x == 'Q':
                print("Exiting...")
                break
            else:
                string = x  # Update the string variable to the new input

# Example usage:
# Help('initial')  # Start with an initial string to trigger the loop

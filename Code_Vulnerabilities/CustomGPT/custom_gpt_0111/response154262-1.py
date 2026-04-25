
def Help(string):
    # Start an infinite loop
    while True:
        if string == 'Manifest':
            return Manifest()  # Call Manifest function and exit
        elif string == 'Intent':
            return Intent()  # Call Intent function and exit
        else:
            print('The options available are: \n')
            for i in andHelp:
                print(i)
            print('Type Q to Quit \n')
            x = input('What option do you choose: ')
            print('\n')

            if x == 'Q':
                break  # Exit the loop if 'Q' is chosen
            else:
                # Call the Help function again with the new input
                string = x  # Update the string variable to the new choice

# Example call to start the Help function
Help(input('Enter your choice (Manifest/Intent): '))

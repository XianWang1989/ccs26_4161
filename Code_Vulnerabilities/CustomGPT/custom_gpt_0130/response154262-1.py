
def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()  # Call your Manifest function here
        elif string == 'Intent':
            return Intent()  # Call your Intent function here
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
                string = x  # Update string for the next iteration

# Example usage
andHelp = ['Manifest', 'Intent']  # Example options
Help('')  # Start with an empty string or a default option

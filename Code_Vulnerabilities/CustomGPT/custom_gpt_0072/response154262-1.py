
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
            x = input('What option do you choose: ').strip()
            print('\n')
            if x == 'Q':
                break
            else:
                string = x  # Update the string variable for the next iteration

# Example usage
andHelp = ['Manifest', 'Intent']

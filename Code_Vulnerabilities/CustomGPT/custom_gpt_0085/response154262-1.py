
def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()  # Correctly exits the function
        elif string == 'Intent':
            return Intent()  # Correctly exits the function
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
                Help(x)  # This call doesn't exit the current instance
                return  # Added to ensure we exit after calling Help(x)

# Example usage:
andHelp = ['Manifest', 'Intent']

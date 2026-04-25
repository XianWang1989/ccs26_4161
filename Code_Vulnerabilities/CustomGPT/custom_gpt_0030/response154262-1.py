
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
                break
            else:
                # Instead of calling Help(x), we assign x to string
                string = x  

# Example usage
andHelp = ['Manifest', 'Intent']  # Replace with actual options
# You would also need to define the Manifest and Intent functions for the code to work.

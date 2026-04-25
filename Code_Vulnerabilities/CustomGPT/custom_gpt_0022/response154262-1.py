
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
                # Update 'string' to keep the loop going
                string = x

# Example usage of the updated function
andHelp = ['Intent', 'Manifest']  # Your available options

def Manifest():
    return "You chose Manifest!"

def Intent():
    return "You chose Intent!"

# Initial call
Help("Start")

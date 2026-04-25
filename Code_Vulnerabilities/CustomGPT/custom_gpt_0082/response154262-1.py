
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
                string = x  # Update `string` to the new input

# Example potential function implementations
def Manifest():
    return "Manifest function executed."

def Intent():
    return "Intent function executed."

# Example options for demonstration
andHelp = ["Intent", "Manifest", "Other Options"]

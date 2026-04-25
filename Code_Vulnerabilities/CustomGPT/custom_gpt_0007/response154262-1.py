
def Help():
    while True:
        x = input('What option do you choose (or type Q to Quit): ')

        if x == 'Manifest':
            return Manifest()
        elif x == 'Intent':
            return Intent()
        elif x == 'Q':
            break
        else:
            print('The options available are: \n')
            for i in andHelp:
                print(i)
            print('Please choose again or type Q to Quit \n')

# Now call Help() without passing parameters
Help()


def path_sel():
    while True:  # Keep asking until a valid path is provided
        path = raw_input("Select desired working directory: ")
        b = []
        ftp.retrlines('LIST', b.append)

        if path not in b:
            print "ERROR- Directory does not exist.\n"
        else:
            print '\nChanging to ' + path, '\n'
            ftp.cwd(path)
            print path
            ftp.retrlines('LIST')
            c = []
            ftp.retrlines('LIST', c.append)
            if 'd' in str(c[0]):
                print "You are in a directory, please select another directory."
                continue  # Repeats the loop if the selected path is also a directory
            break  # Exit the loop if a valid path is selected

    file_dl()  # Proceed to file downloading

# Call your modified path_sel function
path_sel()

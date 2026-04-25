
def path_sel():
    while True:
        path = raw_input("Select desired working directory: ")
        b = []
        ftp.retrlines('LIST', b.append)  # Fetch the list of directories

        if path not in b:
            print "ERROR - Directory does not exist.\n"
        else:
            print '\nChanging to ' + path + '\n'
            ftp.cwd(path)
            print path
            c = []
            ftp.retrlines('LIST', c.append)  # Check the contents of the directory

            # Check if the first item in the list is a directory
            if any('d' in item for item in c):  # Improved check for directories
                print "It seems like this is a directory."
                continue  # Re-prompt the user if this is a directory
            else:
                break  # Exit the loop if successful

file_dl()

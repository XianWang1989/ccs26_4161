
def path_sel():
    while True:  # Loop until a valid path is provided
        path = raw_input("Select desired working directory: ")
        b = []  # List to store directory names returned by FTP
        ftp.retrlines('LIST', b.append)

        if path not in b:
            print "ERROR - Directory does not exist.\n"
        else:
            print '\nChanging to ' + path, '\n'
            ftp.cwd(path)  # Change the working directory
            print path
            c = []  # List to check for a valid directory again
            ftp.retrlines('LIST', c.append)

            # Check if the first item in the list is a directory
            if 'd' in str(c[0]):
                print "The chosen directory is a valid directory."
            break  # Exit the loop when a valid path is entered

# Call the function to select the directory
path_sel()
file_dl()  # Assuming this function downloads files


def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)  # Retrieve the list of directories

    if path not in b:
        print("ERROR- Directory does not exist.\n")
        path_sel()  # Re-ask for the directory until a valid one is provided
    else:
        print('\nChanging to ' + path, '\n')
        ftp.cwd(path)  # Change the working directory
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)  # Again, retrieve the list of directories

        # Check if the first item in the list is a directory ('d' prefix)
        if 'd' in str(c[0]):
            print ("The selected path is a directory. Asking for the new directory again.")
            path_sel()  # Re-ask for the directory if it is indeed a directory
        else:
            print("This path is not a directory. Proceeding with file download.")
            file_dl()  # Proceed with file download as planed

# Initiate the function
path_sel()

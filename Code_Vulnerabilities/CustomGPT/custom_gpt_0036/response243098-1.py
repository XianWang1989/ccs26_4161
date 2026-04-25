
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []

    # Fetch the directory listing from the FTP server
    ftp.retrlines('LIST', b.append)

    if path not in b:
        print("ERROR- Directory does not exist.\n")
        # Ask for the directory again without continuing the recursion
        return path_sel()  # This recursive call still captures the user's input

    # If the path exists, change to that directory
    print('\nChanging to ' + path + '\n')
    ftp.cwd(path)
    print(path)

    # Fetch and print the new directory listing
    c = []
    ftp.retrlines('LIST', c.append)

    # Check if the first item in the list is a directory
    if 'd' in str(c[0]):
        return path_sel()  # Again, we allow the re-ask of a directory if necessary

    file_dl()  # Proceed to download files if the input was valid


# You may want to ensure that this function is called in your main code
# before working with any files.
path_sel()

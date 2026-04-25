
def path_sel():
    path = input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    if path not in b:
        print("ERROR - Directory does not exist.\n")
        return path_sel()  # Return the recursive call

    print('\nChanging to ' + path + '\n')
    ftp.cwd(path)
    print(path)

    c = []
    ftp.retrlines('LIST', c.append)

    if 'd' in str(c[0]):  # Check if the first item in the list indicates a directory
        return path_sel()  # Again, return the recursive call to allow another selection

    # If it gets past this point, proceed with downloading files
    file_dl()

# Example of how you might structure the FTP connection and call the function
# ftp = FTP('ftp.example.com')  # Setup your FTP connection here
# path_sel()  # Start the directory selection process

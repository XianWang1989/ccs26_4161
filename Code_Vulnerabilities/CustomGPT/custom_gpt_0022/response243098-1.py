
def path_sel():
    path = input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    if path not in b:
        print("ERROR - Directory does not exist.\n")
        path_sel()  # Re-ask for input
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if the first item in the list starts with 'd' to see if it's a directory
        if c and 'd' in str(c[0]):
            path_sel()  # Re-ask for input if it's a directory

# Call the function to start
path_sel()
file_dl()

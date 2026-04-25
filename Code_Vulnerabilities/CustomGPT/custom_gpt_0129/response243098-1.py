
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    if path not in b:
        print("ERROR - Directory does not exist.\n")
        path_sel()  # Call the function again to re-ask
        return  # Add return here to exit if the directory doesn't exist

    print('\nChanging to ' + path, '\n')
    ftp.cwd(path)
    print(path)

    # Check if the first item in the list of directories is indeed a directory
    c = []
    ftp.retrlines('LIST', c.append)
    if 'd' in str(c[0]):
        path_sel()  # Call the function again if the first item is a directory

    file_dl()  # Call this function after selecting a valid path

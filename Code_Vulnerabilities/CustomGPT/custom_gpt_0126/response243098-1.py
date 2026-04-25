
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Check if the path exists in the retrieved directory list
    if not any(path in line for line in b):
        print("ERROR - Directory does not exist.\n")
        path_sel()  # Recursively ask for input again
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if the first item has a directory indicator
        if 'd' in str(c[0]):
            path_sel()  # If it's a directory, ask for a new path

file_dl()

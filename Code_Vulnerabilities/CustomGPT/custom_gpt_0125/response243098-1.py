
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Normalize directory names by stripping whitespace and converting to lowercase
    b = [dir.strip().lower() for dir in b]  
    if path.lower() not in b:
        print("ERROR - Directory does not exist.\n")
        path_sel()
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if 'd' is in the first element of the retrieved directory listing
        if 'd' in str(c[0]):
            path_sel()

file_dl()

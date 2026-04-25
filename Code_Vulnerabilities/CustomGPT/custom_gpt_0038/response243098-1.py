
def path_sel():
    path = input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    if path not in b:
        print("ERROR - Directory does not exist.\n")
        return  # Exit the function instead of calling it again

    print('\nChanging to ' + path + '\n')
    ftp.cwd(path)
    print(path)
    c = []
    ftp.retrlines('LIST', c.append)

    # Check for directory condition
    if 'd' in str(c[0]):
        path_sel()  # Optional, only if you want to keep asking for a subdirectory

file_dl()


def path_sel():
    path = input("Select desired working directory: ")  # Use input() for Python 3
    b = []
    ftp.retrlines('LIST', b.append)

    if path not in b:
        print("ERROR - Directory does not exist.\n")
        path_sel()  # Re-ask user for directory
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if 'd' is in any of the directory entries
        if any('d' in entry for entry in c):
            path_sel()  # Re-ask if there's a directory

file_dl()


def path_sel():
    path = input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    if path not in b:
        print("ERROR - Directory does not exist.\n")
        path_sel()  # re-ask the user
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if the first item in the list contains 'd'
        if any('d' in line for line in c):
            path_sel()  # re-ask for a directory if it's a directory

file_dl()

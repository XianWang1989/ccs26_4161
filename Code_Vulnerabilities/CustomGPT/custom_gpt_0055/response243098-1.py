
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Normalize the directory names for comparison
    dir_list = [line.split()[-1] for line in b]  # Get only the directory names from the list

    if path not in dir_list:
        print("ERROR- Directory does not exist.\n")
        path_sel()
    else:
        print('\nChanging to ' + path, '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)
        if any('d' in line for line in c):  # Check if any line indicates a directory
            path_sel()

file_dl()


def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Extract just the directory names from the list entries
    directory_names = [entry.split()[-1] for entry in b]

    if path not in directory_names:
        print("ERROR - Directory does not exist.\n")
        path_sel()
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)
        if 'd' in str(c[0]):
            path_sel()

file_dl()

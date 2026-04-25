
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Normalize entries in b to check against user input
    b = [line.split()[-1] for line in b]  # Extract only the directory names

    if path not in b:
        print("ERROR - Directory does not exist.\n")
        path_sel()
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        ftp.retrlines('LIST')
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if 'c' contains directories (modify this check as needed)
        if any('d' in line for line in c):
            path_sel()

file_dl()

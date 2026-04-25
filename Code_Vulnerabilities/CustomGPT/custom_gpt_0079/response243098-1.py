
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Normalize directory names
    b = [line.split()[-1] for line in b]  # Extract only the directory names

    if path not in b:
        print("ERROR - Directory does not exist.\n")
        path_sel()  # Re-ask for input
    else:
        print('\nChanging to ' + path, '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)
        c = [line.split()[-1] for line in c]  # Normalize this list as well

        # Check if the first line in 'c' indicates a directory
        if 'd' in str(c[0]):
            path_sel()  # Re-ask for input if it's a directory

file_dl()

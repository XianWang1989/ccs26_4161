
def path_sel():
    path = input("Select desired working directory: ")  # Use input() for Python 3
    b = []
    ftp.retrlines('LIST', b.append)

    if path not in b:
        print("ERROR - Directory does not exist.\n")  # Updated print for Python 3
        path_sel()
    else:
        print('\nChanging to ' + path, '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if the first item in the list is a directory
        if any('d' in line for line in c):  # Improved directory check
            path_sel()

    file_dl()

# Ensure to replace `raw_input` with `input` for Python 3

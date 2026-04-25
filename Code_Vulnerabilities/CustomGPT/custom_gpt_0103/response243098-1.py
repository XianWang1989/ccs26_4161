
def path_sel():
    path = input("Select desired working directory: ").strip()
    b = []
    ftp.retrlines('LIST', b.append)

    # Normalize directory names for comparison
    b = [item.strip() for item in b]  # Strip whitespace from each item in b

    if path not in b:
        print("ERROR - Directory does not exist.\n")
        path_sel()
    else:
        print('\nChanging to ' + path, '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)

        if any('d' in line for line in c):  # Check for any directory in the list
            path_sel()

file_dl()

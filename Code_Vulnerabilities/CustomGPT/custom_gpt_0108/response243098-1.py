
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Strip whitespace from entries in the list to ensure comparison works
    b = [entry.strip() for entry in b]

    if path not in b:
        print("ERROR - Directory does not exist.\n")
        path_sel()
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)

        # Check for directory
        if any('d' in entry for entry in c):  # Adjusted condition
            path_sel()

file_dl()

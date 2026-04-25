
def path_sel():
    path = raw_input("Select desired working directory: ").strip()
    b = []
    ftp.retrlines('LIST', b.append)

    # Normalize the listed directories by stripping whitespace
    b = [x.strip() for x in b]

    if path not in b:
        print("ERROR - Directory does not exist.\n")
        path_sel()
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)

        # Check for directory in a normalized fashion
        c = [x.strip() for x in c]
        if 'd' in str(c[0]):
            path_sel()

    file_dl()


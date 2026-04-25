
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Debugging: Print the list of directories
    print("Directories available: ", b)

    # Strip whitespace to avoid formatting issues
    if path.strip() not in [dir.strip() for dir in b]:
        print("ERROR - Directory does not exist.\n")
        path_sel()
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        ftp.retrlines('LIST')
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if the first entry indicates a directory
        if len(c) > 0 and 'd' in str(c[0]):
            path_sel()

    file_dl()


def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Normalize the directory names by stripping whitespace
    if path.strip() not in [dir.strip() for dir in b]:
        print("ERROR - Directory does not exist.\n")
        return path_sel()  # Use return to handle recursion cleanly
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)

        # Check if the first item in c is a directory
        c = []
        ftp.retrlines('LIST', c.append)
        if any('d' in line for line in c):  # Check all lines for 'd'
            return path_sel()  # Again, return for recursion
    file_dl()

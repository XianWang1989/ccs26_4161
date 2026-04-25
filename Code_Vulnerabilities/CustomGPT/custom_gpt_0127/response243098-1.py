
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    if path not in b:
        print("ERROR - Directory does not exist.\n")
        return path_sel()  # Use return to avoid further execution

    print('\nChanging to ' + path + '\n')
    ftp.cwd(path)
    print(path)

    # Check if the first entry in the directory list is a directory
    c = []
    ftp.retrlines('LIST', c.append)

    if 'd' in str(c[0]):
        print("Path is a directory, reselecting...")
        return path_sel()  # Use return here as well for clarity

# Call the function initially
path_sel()
file_dl()

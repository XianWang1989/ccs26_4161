
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Clean up the list of directories
    directories = [line.split()[-1] for line in b]  # Assuming the last element is the directory name

    if path not in directories:
        print("ERROR - Directory does not exist.\n")
        path_sel()
    else:
        print('\nChanging to ' + path, '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if the first item in the list indicates it's a directory
        if 'd' in str(c[0]):
            print("This is a directory. Navigating further...")
            path_sel()

file_dl()

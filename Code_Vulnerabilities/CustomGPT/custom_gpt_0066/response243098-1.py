
def path_sel():
    path = input("Select desired working directory: ")
    b = []

    # Retrieve directory listing
    ftp.retrlines('LIST', b.append)

    # Clean the list to match only directory names
    directories = [line.split()[-1] for line in b if line.startswith('d')]  # assuming 'd' indicates a directory

    if path not in directories:
        print("ERROR - Directory does not exist.\n")
        path_sel()
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        ftp.retrlines('LIST')
        c = []
        ftp.retrlines('LIST', c.append)

        # Check for further directories
        if any('d' in line for line in c):  # Check if any line indicates a directory
            path_sel()

# Call the function to start the process
file_dl()

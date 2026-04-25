
def path_sel():
    path = input("Select desired working directory: ")  # Use input() for Python 3
    b = []
    ftp.retrlines('LIST', b.append)

    # Clean the entries in b to match user input
    directories = [line.split()[-1] for line in b if line.startswith('d')]

    if path not in directories:
        print("ERROR - Directory does not exist.\n")
        path_sel()  # Re-ask for the directory
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        ftp.retrlines('LIST')
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if the current directory is still a directory
        if 'd' in str(c[0]):
            path_sel()  # Re-ask if it's still a directory

# Call the function at the start
file_dl()  # Ensure this function is defined earlier

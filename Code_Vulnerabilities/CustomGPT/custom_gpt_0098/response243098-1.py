
def path_sel():
    path = input("Select desired working directory: ")  # Use input for Python 3
    b = []
    ftp.retrlines('LIST', b.append)

    # Extract just the directory names from the listing
    directories = [line.split()[-1] for line in b if line.startswith('d')]

    if path not in directories:
        print("ERROR - Directory does not exist.\n")
        path_sel()  # Re-ask for input if the directory doesn't exist
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        ftp.retrlines('LIST')

        # Check if the current directory is still a directory
        c = []
        ftp.retrlines('LIST', c.append)
        should_revisit = any('d' in line and line.endswith(path) for line in c)

        if should_revisit:
            path_sel()  # Re-ask for input if it's a directory

# Call the function to start the process
file_dl()

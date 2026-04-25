
def path_sel():
    path = raw_input("Select desired working directory: ").strip()  # Trim whitespace
    b = []
    ftp.retrlines('LIST', b.append)

    # Normalize the directory names in b for comparison
    directories = [line.split()[-1] for line in b]  # Extract the last column which should be the name

    if path not in directories:
        print("ERROR - Directory does not exist.\n")
        path_sel()  # Re-ask the user
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)

        c = []
        ftp.retrlines('LIST', c.append)
        if 'd' in str(c[0]):  # Check if the first line indicates a directory
            path_sel()  # Re-ask if it's a directory

# Call the function to start the process
path_sel()
file_dl()

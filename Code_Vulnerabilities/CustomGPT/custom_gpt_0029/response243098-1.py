
def path_sel():
    path = raw_input("Select desired working directory: ").strip()
    b = []

    # Retrieve the list of directories
    ftp.retrlines('LIST', b.append)

    # Normalize the directory names to check for existence
    directories = [line.split()[-1] for line in b]  # Get the last item in each line (directory name)

    if path not in directories:
        print("ERROR - Directory does not exist.\n")
        path_sel()  # Re-prompt user
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)

        # Check if the current directory has subdirectories
        c = []
        ftp.retrlines('LIST', c.append)
        subdirectories = [line.split()[-1] for line in c if line.startswith('d')]  # Only directories
        if any(d in subdirectories for d in ['your_subdirectory_check']):  # Replace with actual check
            path_sel()  # Re-prompt user if condition is met

file_dl()

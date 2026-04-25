
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Normalize the directory listing for comparison
    directories = [line.split()[-1] for line in b if line.startswith('d')]

    if path not in directories:
        print("ERROR - Directory does not exist.\n")
        path_sel()  # Re-prompt user for input
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)

        # Verify if the current path has directories
        c = []
        ftp.retrlines('LIST', c.append)
        if any('d' in line for line in c):
            path_sel()  # Re-prompt if there are subdirectories

# Call the function
file_dl()

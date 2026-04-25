
def path_sel():
    path = input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    if path not in b:
        print("ERROR - Directory does not exist.\n")
        return path_sel()  # Use return to get the value from recursion
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if the current directory is a folder
        if any('d' in line for line in c):
            return path_sel()  # Handle gracefully if conditions require re-selection

    file_dl()

# Call this function to start the process
path_sel()

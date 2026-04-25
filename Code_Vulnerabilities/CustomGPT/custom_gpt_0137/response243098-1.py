
def path_sel():
    # Get the desired working directory from the user
    path = input("Select desired working directory: ")

    b = []
    ftp.retrlines('LIST', b.append)

    # Clean up the list for better matching
    b = [entry.strip() for entry in b]  # Strip extra whitespace from each entry

    if path not in b:
        print("ERROR- Directory does not exist.\n")
        path_sel()  # Re-ask for a directory if not found
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)  # Change working directory
        print(path)
        ftp.retrlines('LIST')
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if directories exist within the current working directory
        if any('d' in str(line) for line in c):  # Use any to check for any directory in the list
            path_sel()  # Recall if a directory is found

file_dl()

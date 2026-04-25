
def path_sel():
    path = raw_input("Select desired working directory: ").strip()  # Trim whitespace
    b = []
    ftp.retrlines('LIST', b.append)  # Get the list of directories

    # Check if the path exists in the directory list
    if path not in [entry.strip() for entry in b]:  # Strip each entry for comparison
        print("ERROR - Directory does not exist.\n")
        path_sel()  # Re-ask if the path doesn't exist
    else:
        print('\nChanging to ' + path, '\n')
        ftp.cwd(path)  # Change working directory
        print(path)
        ftp.retrlines('LIST')
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if the first entry is a directory
        if 'd' in str(c[0]):
            path_sel()  # Re-ask if the path is a directory

file_dl()

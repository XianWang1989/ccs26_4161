
def path_sel():
    path = input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Normalize the directory names by stripping extra spaces
    b = [dir_entry.strip() for dir_entry in b]

    if path not in b:
        print("ERROR - Directory does not exist.\n")
        path_sel()  # Re-prompt the user
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        ftp.retrlines('LIST')
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if the first entry is a directory
        if 'd' in str(c[0]):
            path_sel()  # Re-prompt if the entry is a directory

# Example function call
file_dl()  # Assuming this function exists elsewhere

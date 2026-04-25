
def path_sel():
    path = input("Select desired working directory: ")
    b = []

    # Retrieve the list of directories
    ftp.retrlines('LIST', b.append)

    # Check if the input path is in the list
    if path not in b:
        print("ERROR - Directory does not exist.\n")
        return path_sel()  # Re-prompt the user for a valid directory
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)

        # Check if the first entry is a directory
        c = []
        ftp.retrlines('LIST', c.append)

        if 'd' in str(c[0]):
            return path_sel()  # Re-prompt if it's a directory

    return path  # Return the valid path for further use

# Call the file download function after selecting the path
file_dl()

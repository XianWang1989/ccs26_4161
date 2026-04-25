
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    if path not in b:
        print("ERROR- Directory does not exist.\n")
        return path_sel()  # Ensure it returns the new path

    print('\nChanging to ' + path, '\n')
    ftp.cwd(path)
    print(path)

    c = []
    ftp.retrlines('LIST', c.append)

    if any('d' in line for line in c):  # Check if any entry is a directory
        return path_sel()  # Return the new path if needed

    return path  # Return the valid path

# Example call
selected_path = path_sel()
file_dl(selected_path)  # Make sure to pass the selected path to the file_dl function


def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Check if the path is in the list
    if path not in b:
        print("ERROR - Directory does not exist.\n")
        return path_sel()  # Return the result of the recursive call

    print('\nChanging to ' + path, '\n')
    ftp.cwd(path)
    print(path)

    c = []
    ftp.retrlines('LIST', c.append)

    # Check if the first entry in c is a directory
    if 'd' in str(c[0]):
        return path_sel()  # Call recursively if it's a directory

    return path  # Return the valid path when done

# Call the file download function after the path selection
selected_path = path_sel()
file_dl(selected_path)

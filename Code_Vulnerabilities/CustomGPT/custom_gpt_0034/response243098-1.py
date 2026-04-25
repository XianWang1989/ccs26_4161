
def path_sel():
    path = input("Select desired working directory: ")  # Use input() in Python 3
    b = []
    ftp.retrlines('LIST', b.append)

    if path not in b:
        print("ERROR - Directory does not exist.\n")
        return path_sel()  # Return the result to correctly handle the returned path
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if the first item starts with 'd' indicating a directory
        if len(c) > 0 and 'd' in str(c[0]):
            return path_sel()  # Handle potential nested directory structure

    return path  # Return the valid path

# Example usage of file_dl() function after ensuring path selection is valid
selected_path = path_sel()
file_dl()

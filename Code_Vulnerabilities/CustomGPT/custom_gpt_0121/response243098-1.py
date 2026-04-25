
def path_sel():
    path = input("Select desired working directory: ")  # Use input() for Python 3
    b = []
    ftp.retrlines('LIST', b.append)

    if path not in b:
        print("ERROR - Directory does not exist.\n")
        return path_sel()  # Return the result of the recursive call
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)

        if any('d' in line for line in c):  # Check if any directory exists
            return path_sel()  # Repeat the selection if it's a directory

    return path  # Return the selected path if everything is fine

# Example call
selected_path = path_sel()
file_dl(selected_path)  # Pass the selected path to file_dl


def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    if path not in b:
        print("ERROR- Directory does not exist.\n")
        return path_sel()  # Use return to ensure we get the valid path

    print('\nChanging to ' + path, '\n')
    ftp.cwd(path)
    print(path)

    c = []
    ftp.retrlines('LIST', c.append)

    # Check for directories in the retrieved list
    if any('d' in line for line in c):
        return path_sel()  # Ensure to return here as well
    else:
        return path  # Return the valid path if no further directories are found

# Example of calling the function
selected_path = path_sel()
file_dl(selected_path)  # Pass the selected path to subsequent functions as needed


def path_sel():
    path = input("Select desired working directory: ")  # Use input() for Python 3
    b = []
    ftp.retrlines('LIST', b.append)

    if path not in b:
        print("ERROR - Directory does not exist.\n")
        return path_sel()  # Use return to get the value back

    print('\nChanging to ' + path + '\n')
    ftp.cwd(path)
    print(path)
    c = []
    ftp.retrlines('LIST', c.append)

    if any('d' in line for line in c):  # Check for directories in the list
        return path_sel()  # Re-ask if there's a directory condition
    return path  # Return the valid path

# Call the function to initiate the directory selection
selected_path = path_sel()
file_dl(selected_path)  # Pass the selected path to file_dl if needed

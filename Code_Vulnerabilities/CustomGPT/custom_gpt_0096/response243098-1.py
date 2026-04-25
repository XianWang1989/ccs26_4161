
def path_sel():
    path = input("Select desired working directory: ")  # Use input instead of raw_input for Python 3
    b = []
    ftp.retrlines('LIST', b.append)

    # Normalize the directory names for comparison
    b = [dirname.strip() for dirname in b]

    if path not in b:
        print("ERROR - Directory does not exist.\n")  # Corrected the print statement
        return path_sel()  # Use return here to ensure proper flow
    else:
        print('\nChanging to ' + path + '\n')  # Adjusted parentheses
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)
        if any('d' in line for line in c):  # Check for directory in the list
            return path_sel()  # Use return for consistency

    file_dl()

# Example of file_dl function for reference
def file_dl():
    print("Proceeding to download files...")
    # Implementation of downloading files goes here

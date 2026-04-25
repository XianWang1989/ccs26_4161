
def path_sel():
    path = input("Select desired working directory: ")  # Use input() for Python 3
    b = []

    # Populate the list of directories
    ftp.retrlines('LIST', b.append)

    # Normalize the comparison by stripping unwanted characters
    b = [item.split()[-1] for item in b]  # Get just the directory names

    if path not in b:
        print("ERROR - Directory does not exist.\n")
        path_sel()  # Re-ask the user for a directory
    else:
        print('\nChanging to ' + path + '\n')
        ftp.cwd(path)
        print(path)
        ftp.retrlines('LIST')

        c = []
        ftp.retrlines('LIST', c.append)

        # Check if the list contains directories and call path_sel again if needed
        c = [item.split()[-1] for item in c]  # Normalize the directory list
        if 'd' in str(c[0]):  # You might want to adjust this check based on your needs
            path_sel()  # Re-ask for a directory if necessary

# Example usage
file_dl()

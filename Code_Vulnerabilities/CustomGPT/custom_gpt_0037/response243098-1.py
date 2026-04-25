
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Check if the path exists in the directory list
    if path not in b:
        print("ERROR - Directory does not exist.\n")
        path_sel()  # Re-ask for input
    else:
        print('\nChanging to ' + path, '\n')
        ftp.cwd(path)
        print(path)
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if the first item in the list indicates a directory
        if 'd' in str(c[0]):
            path_sel()  # Re-ask for input if it's a directory
        else:
            file_dl()  # Call file_dl if not a directory

# Example function to demonstrate usage 
def file_dl():
    print("Downloading files...")  # Placeholder for your download logic

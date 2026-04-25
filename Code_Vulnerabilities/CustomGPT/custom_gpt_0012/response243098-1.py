
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    if path not in b:
        print("ERROR- Directory does not exist.\n")
        return path_sel()  # Return the result of the recursive call
    else:
        print('\nChanging to ' + path, '\n')
        ftp.cwd(path)
        print(path)
        ftp.retrlines('LIST')

        c = []
        ftp.retrlines('LIST', c.append)

        if 'd' in str(c[0]):
            return path_sel()  # Return the result of the recursive call

    return path  # Return the valid directory at the end

# Function to download files
def file_dl():
    # Implement the logic for downloading files here
    pass

# Call path_sel and save the valid path
selected_path = path_sel()
# Now you can use selected_path for further operations

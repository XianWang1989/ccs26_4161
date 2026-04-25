
def path_sel():
    path = raw_input("Select desired working directory: ").strip()  # Remove any leading/trailing whitespace
    b = []
    ftp.retrlines('LIST', b.append)  # Get the list of directories

    # Normalize the listings for easier comparison
    directories = [line.split()[-1] for line in b if line.startswith('d')]  # Get directories only

    # Check if the path entered is in the normalized directories list
    if path not in directories:
        print "ERROR- Directory does not exist.\n"
        return path_sel()  # Ask again and return the result
    else:
        print '\nChanging to ' + path + '\n'
        ftp.cwd(path)  # Change working directory
        print "Current Directory:", ftp.pwd()  # Optionally print the current directory
        ftp.retrlines('LIST')  # List current directory contents

    return path  # Return the valid directory

def file_dl():
    # Implement your file download logic here
    pass

# Start the directory selection process
selected_path = path_sel()
file_dl()  # Call the file download function after a valid directory is selected

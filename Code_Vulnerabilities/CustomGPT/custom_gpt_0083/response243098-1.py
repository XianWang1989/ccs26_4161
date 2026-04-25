
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Normalize the list of paths for comparison
    valid_paths = [line.split()[-1] for line in b if line]  # Get only the directory names
    if path not in valid_paths:
        print "ERROR - Directory does not exist.\n"
        return path_sel()  # Use return to keep the recursion clean
    else:
        print '\nChanging to ' + path, '\n'
        ftp.cwd(path)
        print path
        c = []
        ftp.retrlines('LIST', c.append)
        if any('d' in line for line in c):  # Check if there's a directory
            return path_sel()  # Continue the selection if it's a directory

    return path  # Return the valid path to use later

# Call the function
valid_directory = path_sel()
file_dl(valid_directory)

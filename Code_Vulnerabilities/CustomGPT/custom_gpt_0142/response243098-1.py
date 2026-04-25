
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []

    # Gather list of directories from the FTP server
    ftp.retrlines('LIST', b.append)

    if path not in b:
        print "ERROR - Directory does not exist.\n"
        # Re-ask the user for a directory
        return path_sel()  # Use return to ensure you come back with a correct path

    else:
        print '\nChanging to ' + path + '\n'
        ftp.cwd(path)
        print path
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if the first line of directory list contains 'd' (indicating a directory)
        if 'd' in str(c[0]):
            print "This is a directory. Re-asking for a directory."
            return path_sel()  # Ensure you're re-prompting if it's a directory

    return path  # Return the valid directory path

# You would then capture the returned path when calling the function
selected_path = path_sel()
file_dl(selected_path)  # Assuming you want to use the selected path in file_dl()

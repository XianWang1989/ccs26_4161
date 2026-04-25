
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Normalize the strings in the list for comparison
    b = [entry.split()[-1] for entry in b]  # Assumes directory name is the last item in the entry

    if path not in b:
        print "ERROR - Directory does not exist.\n"
        path_sel()  # Re-ask the user for a directory
    else:
        print '\nChanging to ' + path, '\n'
        ftp.cwd(path)  # Change working directory
        print path
        ftp.retrlines('LIST')
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if the current directory is a directory or file
        if 'd' in str(c[0]):  # Make sure to appropriately check for directories
            path_sel()  # Re-ask for a directory, if it's a directory

file_dl()  # Assuming this function is defined elsewhere

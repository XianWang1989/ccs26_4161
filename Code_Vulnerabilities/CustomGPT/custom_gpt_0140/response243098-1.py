
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Check if the path exists in the listing
    if path not in b:
        print "ERROR - Directory does not exist.\n"
        return path_sel()  # Use return to ensure the function returns a value

    print '\nChanging to ' + path + '\n'
    ftp.cwd(path)
    print path
    c = []
    ftp.retrlines('LIST', c.append)

    # Check if the first listing entry indicates a directory
    if 'd' in str(c[0]):
        print "This is a directory. Please select a subdirectory."
        return path_sel()  # Keep the return to handle recursion correctly

    # If valid, proceed with downloading files
    file_dl()

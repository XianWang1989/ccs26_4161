
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    if path not in b:
        print "ERROR - Directory does not exist.\n"
        return path_sel()  # Use return to handle the recursion properly
    else:
        print '\nChanging to ' + path, '\n'
        ftp.cwd(path)
        print path
        c = []
        ftp.retrlines('LIST', c.append)

        if any('d' in line for line in c):  # Check if any directory is listed
            return path_sel()  # If it's a directory, re-ask for path

    file_dl()


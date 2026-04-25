
def path_sel():
    path = raw_input("Select desired working directory: ")
    directories = []

    # Populate the directories list with just the names
    ftp.retrlines('LIST', lambda line: directories.append(line.split()[-1]))

    # Check if the entered path is in the list of directory names
    if path not in directories:
        print "ERROR- Directory does not exist.\n"
        path_sel()  # Re-ask for the directory
    else:
        print '\nChanging to ' + path, '\n'
        ftp.cwd(path)
        print path
        ftp.retrlines('LIST')
        c = []
        ftp.retrlines('LIST', c.append)
        if 'd' in str(c[0]):
            path_sel()  # If the first item in c is a directory, re-ask for the path.

file_dl()

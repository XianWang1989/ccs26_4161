
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Extract just the directory names from the listing
    directories = [entry.split()[-1] for entry in b]  # Get the last part of each entry line for folder names

    if path not in directories:
        print "ERROR- Directory does not exist.\n"
        path_sel()
    else:
        print '\nChanging to ' + path, '\n'
        ftp.cwd(path)
        print path
        ftp.retrlines('LIST')
        c = []
        ftp.retrlines('LIST', c.append)

        # Check if the first entry is a directory based on the listing
        if 'd' in str(c[0]):
            path_sel()

file_dl()

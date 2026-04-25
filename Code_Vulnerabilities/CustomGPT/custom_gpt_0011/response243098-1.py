
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Clean up directory names for comparison
    directories = [line.split()[-1] for line in b if line.startswith('d')]  # Assuming 'd' indicates a directory

    if path not in directories:
        print "ERROR- Directory does not exist.\n"
        path_sel()  # Re-ask for directory
    else:
        print '\nChanging to ' + path, '\n'
        ftp.cwd(path)
        print path
        ftp.retrlines('LIST')
        c = []
        ftp.retrlines('LIST', c.append)

        if 'd' in str(c[0]):
            path_sel()  # Call the function again if there's a 'd' in the listing

file_dl()


def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Extract directory names from the listing
    dir_names = [line.split()[-1] for line in b if line.startswith('d')]

    if path not in dir_names:
        print "ERROR - Directory does not exist.\n"
        path_sel()
    else:
        print '\nChanging to ' + path + '\n'
        ftp.cwd(path)
        print path
        ftp.retrlines('LIST')
        c = []
        ftp.retrlines('LIST', c.append)

        if 'd' in str(c[0]):
            path_sel()

file_dl()

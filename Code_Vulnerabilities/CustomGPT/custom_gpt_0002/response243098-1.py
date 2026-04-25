
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)
    if path not in b:
        print "ERROR- Directory does not exist.\n"
        return  # Exit the function if directory does not exist
    else:
        print '\nChanging to ' + path, '\n'
        ftp.cwd(path)
        print path

        ftp.retrlines('LIST')
        c = []
        ftp.retrlines('LIST', c.append)

        if 'd' in str(c[0]):
            path_sel()  # Call again if needed

file_dl()

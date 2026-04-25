
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Process the list to extract directory names
    directory_names = [line.split()[-1] for line in b]  # Adjust this index depending on your FTP listing format

    if path not in directory_names:
        print "ERROR- Directory does not exist.\n"
        path_sel()
    else:
        print '\nChanging to ' + path, '\n'
        ftp.cwd(path)
        print path
        ftp.retrlines('LIST')
        c = []
        ftp.retrlines('LIST', c.append)

        if 'd' in str(c[0]):
            path_sel()

file_dl()

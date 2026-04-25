
def path_sel():
    while True:
        path = raw_input("Select desired working directory: ")
        b = []
        ftp.retrlines('LIST', b.append)

        if path not in b:
            print "ERROR - Directory does not exist.\n"
        else:
            print '\nChanging to ' + path, '\n'
            ftp.cwd(path)
            print path

            # Check if there are directories in the current listing
            c = []
            ftp.retrlines('LIST', c.append)
            if any('d' in line for line in c):
                # If a directory is found, re-select the path
                continue
            else:
                break  # Exit if no directory found

    file_dl()

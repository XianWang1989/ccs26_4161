
def path_sel():
    path = raw_input("Select desired working directory: ")
    b = []
    ftp.retrlines('LIST', b.append)

    # Extract directory names from the server output
    dir_names = [line.split()[-1] for line in b if line.startswith('d')]  # Adjust based on your FTP output

    if path not in dir_names:
        print "ERROR - Directory does not exist.\n"
        path_sel()  # Re-prompt for directory
    else:
        print '\nChanging to ' + path + '\n'
        ftp.cwd(path)
        print path
        ftp.retrlines('LIST')
        c = []
        ftp.retrlines('LIST', c.append)
        if 'd' in str(c[0]):  # Check if the first line of LIST output is a directory
            path_sel()  # Re-prompt if still in a directory

file_dl()

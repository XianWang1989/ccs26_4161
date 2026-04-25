
import os
import stat

def check_permissions(path):
    if os.path.exists(path):
        permissions = stat.filemode(os.stat(path).st_mode)
        print(f"{path}: {permissions}")
    else:
        print(f"{path} does not exist.")

static_files_path = '/path/to/your/static/files'
check_permissions(static_files_path)

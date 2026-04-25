
import sys
import os

# Adjust the site-packages path
site_packages_path = '/opt/myPythonProject/lib/python3.x/site-packages'
if site_packages_path not in sys.path:
    sys.path.append(site_packages_path)

# Your project code
def main():
    print("Hello from my custom Python project!")

if __name__ == '__main__':
    main()

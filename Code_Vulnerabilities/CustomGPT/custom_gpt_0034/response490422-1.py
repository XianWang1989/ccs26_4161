
#!/opt/myPythonProject/python/bin/python

import sys
sys.path.insert(0, '/opt/myPythonProject/mycode')

# Now you can import modules from your mycode directory
import my_module

if __name__ == "__main__":
    my_module.run()

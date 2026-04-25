
import sys
import os

# Adding a specific directory to the PYTHONPATH
sys.path.append('/path/to/your/directory')

# Now you can import modules from the added directory
try:
    import your_module  # Replace 'your_module' with the module you want to import
except ImportError as e:
    print(f"Error importing module: {e}")

# Alternatively, you can use the PYTHONPATH environment variable directly within your script:
os.environ['PYTHONPATH'] = '/path/to/another/directory'

# Now the new PYTHONPATH will also include the specified directory
# You may need to re-import the module if you add it after import

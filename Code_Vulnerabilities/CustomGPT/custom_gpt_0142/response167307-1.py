
import sys
import os

# Define your custom directories
# You can change these to point to your desired source directories
production_dir = '/path/to/your/production/code'
testing_dir = '/path/to/your/testing/code'
submodule_dir = '/path/to/your/git/submodule'

# Add the directories to the sys.path
sys.path.append(production_dir)
sys.path.append(testing_dir)
sys.path.append(submodule_dir)

# Now you can import your modules from these paths
try:
    import your_production_module
    import your_testing_module
    import your_submodule_module

    # Use the modules
    your_production_module.some_function()
    your_testing_module.test_function()
    your_submodule_module.sub_function()

except ImportError as e:
    print(f"Error importing module: {e}")

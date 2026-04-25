
import sys
import os

# Add multiple directories to PYTHONPATH
base_dir = os.path.dirname(os.path.abspath(__file__))
production_dir = os.path.join(base_dir, 'src', 'production')
testing_dir = os.path.join(base_dir, 'src', 'testing')

# Append directories to sys.path
sys.path.append(production_dir)
sys.path.append(testing_dir)

# Now you can import your modules
# from my_module import MyClass  # Example import statement

print("Current PYTHONPATH:", sys.path)

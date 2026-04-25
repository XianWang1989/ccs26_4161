
import sys

# Add different source paths
sys.path.append('/path/to/production/code')
sys.path.append('/path/to/testing/code')

# Now you can import from those paths
try:
    from production_module import feature
    from testing_module import test_feature
except ImportError as e:
    print(f"Import error: {e}")

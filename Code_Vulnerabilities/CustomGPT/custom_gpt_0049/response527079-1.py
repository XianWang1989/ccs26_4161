
from unittest.mock import MagicMock, patch
import unittest

# Assuming this is the function you want to test
def funcToGetBar():
    # This should return an object with some attributes
    pass

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class TestMyFunction(unittest.TestCase):

    @patch('__main__.funcToGetBar')  # Patch the function in the module where it's used
    def testGetBar(self, mocked_func):
        # Create a mocked object
        mocked_bar = MagicMock()
        expected_return_val = [obj1, obj2]  # Replace with your actual objects

        # Set the expected attribute directly
        mocked_bar.some_attr = expected_return_val
        mocked_func.return_value = mocked_bar  # funcToGetBar is patched

        # Call the function
        result = foo()

        # Assert the result
        self.assertEqual(expected_return_val, result)

# In this case, you would replace obj1, obj2 with actual objects you want to return.

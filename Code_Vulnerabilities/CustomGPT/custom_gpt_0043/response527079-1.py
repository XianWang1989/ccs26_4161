
from unittest.mock import MagicMock, patch
import unittest

# Assume we have a function `foo()` defined as follows:
def funcToGetBar():
    # This would normally return an object with attributes
    pass

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class TestFoo(unittest.TestCase):
    @patch('__main__.funcToGetBar')  # Patch the function to control its return value
    def testGetBar(self, mock_func):
        # Create the mocked bar
        mocked_bar = MagicMock()
        expected_return_val = [1, 2, 3]

        # Set the expected return value for the 'some_attr' attribute
        mocked_bar.some_attr = expected_return_val

        # Set the patched function to return the mocked_bar
        mock_func.return_value = mocked_bar

        # Call the function and assert the returned value
        self.assertEqual(expected_return_val, foo())

if __name__ == '__main__':
    unittest.main()

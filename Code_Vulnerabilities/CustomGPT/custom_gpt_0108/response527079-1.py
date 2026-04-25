
from unittest.mock import MagicMock, patch
import unittest

# Mocked function
def funcToGetBar():
    pass

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class TestFoo(unittest.TestCase):
    @patch('__main__.funcToGetBar')  # Adjust the import path as necessary
    def testGetBar(self, mock_func):
        mocked_bar = MagicMock()
        expected_return_val = [object(), object()]  # Use actual objects here

        # Set the expected return value on the mocked_bar's attribute
        mocked_bar.some_attr = expected_return_val
        mock_func.return_value = mocked_bar  # Patch the funcToGetBar return value

        # Call the function and assert
        self.assertEqual(expected_return_val, foo())

if __name__ == '__main__':
    unittest.main()


from unittest.mock import MagicMock, patch
import unittest

# Assume this function we want to test
def funcToGetBar():
    pass  # To be mocked in tests

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class MyTestCase(unittest.TestCase):
    @patch('module_under_test.funcToGetBar')  # Adjust the import path accordingly
    def testGetBar(self, mock_func):
        # Prepare your mock
        mocked_bar = MagicMock()
        expected_return_value = ['obj1', 'obj2']  # Example list

        # Set the attribute directly
        mocked_bar.some_attr = expected_return_value

        # Mock the function to return the mocked object
        mock_func.return_value = mocked_bar

        # Call the function and assert
        self.assertEqual(expected_return_value, foo())

if __name__ == '__main__':
    unittest.main()

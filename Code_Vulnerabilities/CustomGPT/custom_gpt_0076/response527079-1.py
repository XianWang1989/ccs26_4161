
from unittest.mock import MagicMock, patch
import unittest

# Assuming funcToGetBar is defined elsewhere
def funcToGetBar():
    pass

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class TestFoo(unittest.TestCase):
    @patch('__main__.funcToGetBar')  # Adjust the import path if necessary
    def testGetBar(self, mock_func):
        mocked_bar = MagicMock()
        expected_return_val = ['obj1', 'obj2']  # Example list

        # Set 'some_attr' on the mocked_bar
        mocked_bar.some_attr = expected_return_val
        mock_func.return_value = mocked_bar  # Patch the return value of funcToGetBar

        # Test the function
        self.assertEqual(expected_return_val, foo())

if __name__ == '__main__':
    unittest.main()

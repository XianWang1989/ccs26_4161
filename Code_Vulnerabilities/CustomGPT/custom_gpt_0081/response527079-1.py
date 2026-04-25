
from unittest.mock import MagicMock, patch
import unittest

def funcToGetBar():
    # This function is intended to be mocked in the test
    pass

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class TestFooFunction(unittest.TestCase):

    @patch('__main__.funcToGetBar')  # Adjust this to your import path
    def testGetBar(self, mock_func):
        # Mocked object
        mocked_bar = MagicMock()
        expected_return_val = ['obj1', 'obj2']  # Your expected return value

        # Set the attribute `some_attr` on the mocked bar
        mocked_bar.some_attr = expected_return_val

        mock_func.return_value = mocked_bar  # funcToGetBar is patched

        # Execute the function being tested
        result = foo()

        # Assertion
        self.assertEqual(result, expected_return_val)

if __name__ == '__main__':
    unittest.main()

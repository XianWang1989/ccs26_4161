
from unittest.mock import MagicMock, patch
import unittest

def funcToGetBar():
    # Placeholder for the actual implementation
    pass

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class TestFoo(unittest.TestCase):
    @patch('__main__.funcToGetBar')  # Adjust the patch target if necessary
    def testGetBar(self, mock_func):
        mocked_bar = MagicMock()
        expected_return_val = ['obj1', 'obj2']

        # Directly set the attribute instead of mocking getattr
        mocked_bar.some_attr = expected_return_val  

        mock_func.return_value = mocked_bar

        # Call the function and assert the expected outcome
        self.assertEqual(expected_return_val, foo())

if __name__ == '__main__':
    unittest.main()

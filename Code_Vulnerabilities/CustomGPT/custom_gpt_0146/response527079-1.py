
from unittest.mock import MagicMock, patch
import unittest

# Assuming this is your function
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class TestFoo(unittest.TestCase):
    @patch('__main__.funcToGetBar')  # Update the module name as necessary
    def testGetBar(self, mock_funcToGetBar):
        mocked_bar = MagicMock()
        expected_return_val = ['obj1', 'obj2']  # Your expected output

        # Set the attribute directly on the mocked object
        mocked_bar.some_attr = expected_return_val
        mock_funcToGetBar.return_value = mocked_bar

        # Call the function and assert the expected output
        self.assertEqual(expected_return_val, foo())

if __name__ == '__main__':
    unittest.main()

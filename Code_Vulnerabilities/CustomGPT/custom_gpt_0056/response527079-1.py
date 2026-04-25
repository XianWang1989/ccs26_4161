
from unittest.mock import MagicMock, patch
import unittest

# Function under test
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Patch the function that gets bar
@patch('__main__.funcToGetBar')
class TestFoo(unittest.TestCase):
    def testGetBar(self, mock_func):
        # Prepare the expected return value
        expected_return_val = ['obj1', 'obj2']

        # Create a MagicMock instance for bar
        mocked_bar = MagicMock()
        # Set the attribute directly
        mocked_bar.some_attr = expected_return_val

        # Set the mock to return the mocked_bar when funcToGetBar is called
        mock_func.return_value = mocked_bar

        # Call foo and assert the result
        self.assertEqual(expected_return_val, foo())

# Run the tests
if __name__ == '__main__':
    unittest.main()

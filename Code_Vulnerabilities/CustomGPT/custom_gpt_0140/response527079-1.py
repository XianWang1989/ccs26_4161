
from unittest.mock import MagicMock, patch
import unittest

def funcToGetBar():
    # Original function implementation (mocked in tests)
    pass

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class TestFooFunction(unittest.TestCase):
    @patch('__main__.funcToGetBar')
    def testGetBar(self, mock_func):
        # Create a mock for bar
        mocked_bar = MagicMock()

        # Set the desired attribute directly on the mock
        expected_return_val = [obj1, obj2]
        mocked_bar.some_attr = expected_return_val

        # Patch `funcToGetBar` to return our mocked bar
        mock_func.return_value = mocked_bar

        # Call the function and assert
        self.assertEqual(expected_return_val, foo())

# Run the tests
if __name__ == '__main__':
    unittest.main()

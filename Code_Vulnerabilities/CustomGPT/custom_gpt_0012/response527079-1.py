
from unittest.mock import MagicMock, patch
import unittest

# Assuming this is your function under test
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Sample test case class
class TestFooFunction(unittest.TestCase):
    @patch('__main__.funcToGetBar')
    def testGetBar(self, mock_func):
        # Create a mocked bar
        mocked_bar = MagicMock()

        # This is the value you want returned when accessing some_attr
        expected_return_val = [obj1, obj2]  # replace obj1, obj2 with actual values

        # Set the some_attr attribute on the mocked bar
        mocked_bar.some_attr = expected_return_val

        # Set the return value of the patched funcToGetBar
        mock_func.return_value = mocked_bar

        # Call the function and assert the returned value
        self.assertEqual(expected_return_val, foo())

# Run the test
if __name__ == '__main__':
    unittest.main()

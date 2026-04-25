
from unittest import TestCase
from unittest.mock import MagicMock, patch

# Assuming your function is defined in a module named 'mymodule'
def funcToGetBar():
    # This would be your implementation that gets the bar object
    pass

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class MyTestCase(TestCase):
    @patch('__main__.funcToGetBar')  # Adjust the path as necessary
    def testGetBar(self, mock_func):
        # Create a mocked bar object
        mocked_bar = MagicMock()
        expected_return_val = ['obj1', 'obj2']  # Your expected return value

        # Set the attribute directly on the mock object
        mocked_bar.some_attr = expected_return_val
        mock_func.return_value = mocked_bar  # Patch funcToGetBar

        # Call the function and assert the result
        self.assertEqual(expected_return_val, foo())

# To run the tests, you would typically use a test runner like pytest or unittest

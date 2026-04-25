
from unittest import TestCase
from unittest.mock import MagicMock, patch

# Example function we're testing
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Your test case
class MyTestCase(TestCase):

    @patch('your_module.funcToGetBar')  # replace 'your_module' with the module where funcToGetBar is defined
    def testGetBar(self, mock_func):
        # Create a mock object
        mocked_bar = MagicMock()
        expected_return_value = ["obj1", "obj2"]  # Example objects you expect

        # Set the attribute on the mock object directly
        mocked_bar.some_attr = expected_return_value

        # Set the return value for the patched function
        mock_func.return_value = mocked_bar

        # Execute the function under test
        result = foo()

        # Assert that the result is what you expect
        self.assertEqual(expected_return_value, result)

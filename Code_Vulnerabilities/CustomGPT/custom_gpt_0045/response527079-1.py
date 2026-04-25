
from unittest import TestCase
from unittest.mock import patch, MagicMock

# Assume this is a part of the module you are testing
def funcToGetBar():
    # This function would return an instance in actual code
    pass

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class TestFoo(TestCase):
    @patch('__main__.funcToGetBar')  # Adjust the path according to your module
    def test_get_bar(self, mock_func):
        # Create a mock object
        mocked_bar = MagicMock()

        # Define the expected return value
        expected_return_val = ['obj1', 'obj2']

        # Set the attribute directly on the mocked_bar
        mocked_bar.some_attr = expected_return_val

        # Set the return value of funcToGetBar to our mocked_bar
        mock_func.return_value = mocked_bar

        # Call the function under test
        result = foo()

        # Assert the result is as expected
        self.assertEqual(result, expected_return_val)

# If you run this code as a part of a test suite, it should work correctly.

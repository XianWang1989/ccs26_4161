
from unittest import TestCase
from unittest.mock import MagicMock, patch

# Function to be tested
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class TestFoo(TestCase):

    @patch('module_where_funcToGetBar_is.funcToGetBar')  # Patch the function
    def testGetBar(self, mock_func):
        # Setting up the mock bar
        mocked_bar = MagicMock()
        expected_return_val = [obj1, obj2]  # Replace with actual test objects
        mocked_bar.some_attr = expected_return_val  # Set the attribute directly
        mock_func.return_value = mocked_bar  # Mock the function return value

        # Call the function and assert
        self.assertEqual(expected_return_val, foo())

# Make sure to replace 'module_where_funcToGetBar_is' with the actual module path.

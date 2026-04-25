
from unittest import TestCase
from unittest.mock import patch, MagicMock

# Assuming this is your function
def funcToGetBar():
    # This function would normally return an object
    pass

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class TestFoo(TestCase):

    @patch('__main__.funcToGetBar')  # Adjust the import path as necessary
    def test_get_bar(self, mock_func):
        mocked_bar = MagicMock()
        expected_return_value = ['obj1', 'obj2']

        # Set the 'some_attr' attribute directly on the mocked_bar
        mocked_bar.some_attr = expected_return_value

        # Set the return value of the patched function
        mock_func.return_value = mocked_bar

        # Run the test
        result = foo()
        self.assertEqual(result, expected_return_value)

# To run the tests, you would usually use a test runner or invoke it via the command line

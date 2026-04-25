
from unittest import TestCase
from unittest.mock import MagicMock, patch

# Assuming this is your function
def funcToGetBar():
    # This function would normally return an object
    pass

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class TestFoo(TestCase):
    @patch('__main__.funcToGetBar')
    def test_get_bar(self, mock_func):
        # Create a mock object for bar
        mocked_bar = MagicMock()

        # Define expected return value for the attribute
        expected_return_val = ['obj1', 'obj2']

        # Set the attribute on the mocked object
        mocked_bar.some_attr = expected_return_val

        # Set the return value of the patched function
        mock_func.return_value = mocked_bar

        # Call the function and assert the return value
        result = foo()
        self.assertEqual(expected_return_val, result)

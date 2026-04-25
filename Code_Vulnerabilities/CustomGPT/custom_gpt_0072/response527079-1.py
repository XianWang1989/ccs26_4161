
from unittest import TestCase
from unittest.mock import MagicMock, patch

# Assume this is the function you're testing
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class MyTestCase(TestCase):
    @patch('your_module.funcToGetBar')
    def test_get_bar(self, mock_func):
        # Create a mocked object for bar
        mocked_bar = MagicMock()

        # Set the expected return value for the "some_attr" attribute
        expected_return_val = [obj1, obj2]  # replace obj1 and obj2 with actual objects
        mocked_bar.some_attr = expected_return_val

        # Configure the mock function to return the mocked bar
        mock_func.return_value = mocked_bar

        # Call the function and assert the expected result
        result = foo()
        self.assertEqual(expected_return_val, result)

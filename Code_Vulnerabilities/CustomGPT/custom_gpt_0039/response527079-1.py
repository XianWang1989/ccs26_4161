
from unittest import TestCase
from unittest.mock import patch, MagicMock

# Your function to be tested
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class MyTests(TestCase):

    @patch('your_module.funcToGetBar')  # Adjust the import path accordingly
    def test_get_bar(self, mock_func):
        mocked_bar = MagicMock()
        expected_return_val = [obj1, obj2]  # Set your expected return value here

        # Set the expected return value directly as an attribute
        mocked_bar.some_attr = expected_return_val
        mock_func.return_value = mocked_bar  # Patch funcToGetBar to return mocked_bar

        # Call the function under test
        result = foo()

        # Assert that the result matches the expected return value
        self.assertEqual(result, expected_return_val)

# Run your tests with a test runner of your choice

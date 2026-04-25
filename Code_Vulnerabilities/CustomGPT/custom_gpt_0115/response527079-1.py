
from unittest import TestCase
from unittest.mock import MagicMock, patch

# Assuming this is your function to be tested
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class MyTestCase(TestCase):

    @patch('module_containing_funcToGetBar.funcToGetBar')  # Adjust the import path accordingly
    def test_get_bar(self, mock_func):
        # Create a mock object
        mocked_bar = MagicMock()
        expected_return_val = ['obj1', 'obj2']  # Your expected return value

        # Set the desired attribute on the mocked bar object
        mocked_bar.some_attr = expected_return_val
        mock_func.return_value = mocked_bar  # Patch the function to return the mock

        # Call the function and assert the expected result
        self.assertEqual(expected_return_val, foo())

# Run the tests
if __name__ == '__main__':
    import unittest
    unittest.main()

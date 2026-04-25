
from unittest import TestCase
from unittest.mock import patch, MagicMock

# Suppose this is your function to test
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class MyTestCase(TestCase):

    @patch('your_module.funcToGetBar')  # Adjust the import path accordingly
    def testGetBar(self, mock_func):
        mocked_bar = MagicMock()
        expected_return_val = [obj1, obj2]  # Your expected return value
        mocked_bar.some_attr = expected_return_val  # Set the attribute directly
        mock_func.return_value = mocked_bar  # Patch the function to return the mock

        result = foo()  # Call the function under test
        self.assertEqual(result, expected_return_val)  # Assert the expected return value

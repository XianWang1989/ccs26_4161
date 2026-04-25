
from unittest import TestCase
from unittest.mock import MagicMock, patch

# Assume foo() is defined in the module you're testing
# from your_module import foo

def funcToGetBar():
    pass  # This is the function you want to mock

class TestFoo(TestCase):
    @patch('__main__.funcToGetBar')  # Change to your module path
    def testGetBar(self, mock_func):
        mocked_bar = MagicMock()
        expected_return_val = ["obj1", "obj2"]

        # Set the attribute directly on the mocked object
        mocked_bar.some_attr = expected_return_val

        # Configure the mock to return your mocked_bar
        mock_func.return_value = mocked_bar

        # Call the function under test
        result = foo()

        # Assert the expected return value
        self.assertEqual(expected_return_val, result)


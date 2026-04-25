
from unittest.mock import MagicMock, patch
import unittest

# The function you're testing
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Example test case
class TestFoo(unittest.TestCase):

    @patch('your_module.funcToGetBar')  # Adjust the import path accordingly
    def test_get_bar(self, mock_func):
        # Creating the MagicMock object
        mocked_bar = MagicMock()
        expected_return_val = ['obj1', 'obj2']  # Your expected list

        # Set the attribute directly on the mocked object
        mocked_bar.some_attr = expected_return_val

        # Assign the mocked bar to the patched function
        mock_func.return_value = mocked_bar

        # Run the function under test
        result = foo()

        # Check if the result matches the expected
        self.assertEqual(expected_return_val, result)

if __name__ == '__main__':
    unittest.main()

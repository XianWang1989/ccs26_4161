
from unittest.mock import MagicMock, patch
import unittest

# Assuming this is your function to test
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class TestGetBar(unittest.TestCase):
    @patch('your_module.funcToGetBar')  # Replace 'your_module' with the name of your module
    def test_get_bar(self, mock_func):
        mocked_bar = MagicMock()
        expected_return_val = ['obj1', 'obj2']  # Your expected return values

        # Set `some_attr` on the mocked bar
        mocked_bar.some_attr = expected_return_val

        # Assign the mocked bar to the patched `funcToGetBar`
        mock_func.return_value = mocked_bar

        # Call the function we're testing
        result = foo()

        # Verify the result
        self.assertEqual(expected_return_val, result)

# Run the tests
if __name__ == '__main__':
    unittest.main()

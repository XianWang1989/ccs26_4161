
from unittest.mock import MagicMock, patch
import unittest

# Assume this is your function to be tested:
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class TestFoo(unittest.TestCase):

    @patch('your_module.funcToGetBar')  # Replace 'your_module' with the actual module name
    def test_get_bar(self, mock_func):
        # Setting up the mock object
        mocked_bar = MagicMock()
        expected_return_val = [obj1, obj2]  # Replace with your actual expected values

        # Setting the attribute directly on the mocked object
        mocked_bar.some_attr = expected_return_val
        mock_func.return_value = mocked_bar

        # Call the function and assert the result
        result = foo()
        self.assertEqual(expected_return_val, result)

# Running the tests
if __name__ == '__main__':
    unittest.main()

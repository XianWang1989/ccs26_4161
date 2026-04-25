
from unittest import TestCase
from unittest.mock import patch, MagicMock

# Example function to be tested
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Your test class
class TestFoo(TestCase):
    @patch('your_module.funcToGetBar')  # Adjust the module path as necessary
    def test_get_bar(self, mock_func):
        # Create a mock object
        mocked_bar = MagicMock()
        expected_return_val = ['obj1', 'obj2']  # Your expected return value

        # Set the attribute directly on the mock
        mocked_bar.some_attr = expected_return_val

        # Use the mock in the patched function
        mock_func.return_value = mocked_bar

        # Call the function and assert the result
        self.assertEqual(expected_return_val, foo())

# To run the tests
if __name__ == '__main__':
    import unittest
    unittest.main()
